import psycopg2
from contextlib import closing
from psycopg2 import sql as sql1

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui1 import Ui_MainWindow
from mainWindow import Ui_MainWindow1
from showTable import Ui_Table
from PyQt5.QtWidgets import QMessageBox

import datetime
import pytz


class ShowTable(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShowTable, self).__init__()
        self.main = None
        self.ui = Ui_Table()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Table")
        self.setWindowIcon(QIcon('book3.jpg'))
        self.ui.loadButton.clicked.connect(self.load)
        self.ui.backButton.clicked.connect(self.back)

    def back(self):
        self.main = MainWindow()
        self.main.show()
        self.close()

    def load(self):
        with closing(psycopg2.connect(dbname='Diary', user='postgres',
                                      password='MAtienko9999', host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM questions")
                self.ui.tableWidget.setRowCount(0)
                for row_number, row in enumerate(cursor.fetchall()):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.diary = None
        self.table = None
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main")
        self.setWindowIcon(QIcon('book3.jpg'))
        self.ui.addButton.clicked.connect(self.add)
        self.ui.showButton.clicked.connect(self.show1)

    def add(self):
        self.diary = Diary()
        self.diary.show()
        self.close()

    def show1(self):
        self.table = ShowTable()
        self.table.show()
        self.close()


class Diary(QtWidgets.QMainWindow):
    def __init__(self):
        super(Diary, self).__init__()
        self.main = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Diary")
        self.setWindowIcon(QIcon('book3.jpg'))

        self.ui.lineEdit.setPlaceholderText("Да/Нет")
        self.ui.lineEdit_2.setPlaceholderText("Да/Нет")
        self.ui.lineEdit_3.setPlaceholderText("Да/Нет")
        self.ui.lineEdit_4.setPlaceholderText("Да/Нет")
        self.ui.lineEdit_5.setPlaceholderText("Да/Нет")

        self.ui.pushButton.clicked.connect(self.write_answer)
        self.ui.back.clicked.connect(self.back)
        pass

    def back(self):
        self.main = MainWindow()
        self.main.show()
        self.close()

    def write_answer(self):
        try:
            callisthenics = (self.ui.lineEdit.text()).lower()
            bed = self.ui.lineEdit_2.text()
            stuffs = self.ui.lineEdit_3.text()
            dish = self.ui.lineEdit_4.text()
            aim_of_the_day = self.ui.textEdit.toPlainText()
            execute = self.ui.lineEdit_5.text()
            initiative = self.ui.textEdit_2.toPlainText()
            good_things = self.ui.textEdit_3.toPlainText()
            bad_things = self.ui.textEdit_4.toPlainText()
            new = self.ui.textEdit_5.toPlainText()
            job_time = self.ui.textEdit_6.toPlainText()
            pe = self.ui.textEdit_7.toPlainText()
            meditation = self.ui.textEdit_8.toPlainText()
            thanks = self.ui.textEdit_9.toPlainText()
            charity = self.ui.textEdit_10.toPlainText()
            # charity = round(float(charity), 2)
            give_up = self.ui.textEdit_11.toPlainText()
            tommorow_things = self.ui.textEdit_12.toPlainText()

            callisthenics = True if callisthenics in ['да', 'была', '+'] else False
            execute = True if execute in ['да', 'была', '+', 'Выполнена', 'выполнена'] else False
            bed = True if bed in ['да', 'была', '+'] else False
            stuffs = True if stuffs in ['да', 'была', '+'] else False
            dish = True if dish in ['да', 'была', '+'] else False
            job_time = True if job_time in ['да', 'была', '+'] else False
            pe = True if pe in ['да', 'была', '+'] else False
            meditation = True if meditation in ['да', 'была', '+'] else False

            charity = 0 if charity == '' else charity

            with closing(psycopg2.connect(dbname='Diary', user='postgres',
                                          password='MAtienko9999', host='localhost')) as conn:
                with conn.cursor() as cursor:

                    ##-- get last id
                    cursor.execute("SELECT id FROM questions order by id DESC")
                    try:
                        last_id = cursor.fetchone()[0]
                    except TypeError:
                        last_id = 0

                    ##-- write answers
                    now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
                    sql = "INSERT INTO questions (id, date, callisthenics, bed, stuffs, dish, aim_of_the_day, \
                            execute, initiative, good_things, bad_things, \
                            new, job_time, pe, meditation, thanks, charity, \
                            give_up, tommorow_things) VALUES (%s, '%s', %s, %s, \
                            %s, %s, '%s', %s, '%s', '%s', '%s', '%s', \
                            '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                          % (last_id+1, datetime.datetime.now(pytz.timezone("Europe/Moscow")), \
                            callisthenics, bed, stuffs, dish, aim_of_the_day, \
                            execute, initiative, good_things, bad_things, \
                            new, job_time, pe, meditation, thanks, charity, give_up, tommorow_things)
                    cursor.execute(sql)

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Записано в БД")
                    msg.exec()

                    #cursor.execute("SELECT * FROM questions")
                    #for row in cursor.fetchall():
                    #    print(row)
                    # for row in cursor:
                    #     print(row)

                    conn.commit()
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!')
            error_dialog.exec()
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())
