import psycopg2
from contextlib import closing
from psycopg2 import sql as sql1

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui1 import Ui_MainWindow

import datetime
import pytz

class Diary(QtWidgets.QMainWindow):
    def __init__(self):
        super(Diary, self).__init__()
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
        pass

    def write_answer(self):
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

                print("Запись произведена")
                #cursor.execute("SELECT * FROM questions")
                #for row in cursor.fetchall():
                #    print(row)
                # for row in cursor:
                #     print(row)

                conn.commit()
        pass


app = QtWidgets.QApplication([])
application = Diary()
application.show()
sys.exit(app.exec())





