# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -3115, 752, 4081))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #f00;\n"
"color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 4000))
        self.frame.setStyleSheet("background-color: #fbff00\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_3.addWidget(self.textEdit_4)
        self.label_15 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_3.addWidget(self.textEdit_5)
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_3.addWidget(self.textEdit_6)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_3.addWidget(self.textEdit_7)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.textEdit_8 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_3.addWidget(self.textEdit_8)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.textEdit_9 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_3.addWidget(self.textEdit_9)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.textEdit_10 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayout_3.addWidget(self.textEdit_10)
        self.label_21 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.textEdit_11 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_11.setObjectName("textEdit_11")
        self.verticalLayout_3.addWidget(self.textEdit_11)
        self.label_22 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.textEdit_12 = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setStyleSheet("color: black;\n"
"background-color: #ffffff;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.textEdit_12.setObjectName("textEdit_12")
        self.verticalLayout_3.addWidget(self.textEdit_12)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Romanow,sans-serif")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 0, 0);\n"
"    text-decoration: none;\n"
"    border: 3px solid #218294;\n"
"    background-color: #ffffff;\n"
"    display: block;\n"
"    text-transform: uppercase;\n"
"    position: relative;\n"
"    transition: 0.5s;\n"
"    overflow: hidden;\n"
"    font-family: Times New Romanow, sans-serif;\n"
"font-size: 30px;\n"
"}\n"
"\n"
"QPushButton::before,\n"
"QPushButton::after {\n"
"    position: absolute;\n"
"    content: \'\';\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    background: #218294;\n"
"    top: 0;\n"
"    left: -100%;\n"
"    opacity: 0.5;\n"
"    transition: 0.3s;\n"
"    z-index: -1;\n"
"}\n"
"\n"
"QPushButton::after {\n"
"    opacity: 1;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QPushButton:hover::before,\n"
"QPushButton:hover::after {\n"
"    left: 0;\n"
"    transition-delay: .2s;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    background-color: rgb(81, 12, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Дневник"))
        self.label_2.setText(_translate("MainWindow", "Зарядка сделана?"))
        self.label_4.setText(_translate("MainWindow", "Кровать сразу заправлена?"))
        self.label_6.setText(_translate("MainWindow", "Вещи на своих местах лежат?"))
        self.label_8.setText(_translate("MainWindow", "Посуда чистая?"))
        self.label_10.setText(_translate("MainWindow", "Опишите задачу дня:"))
        self.label_11.setText(_translate("MainWindow", "Выполнена или нет?"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Три места, где вы сегодня проявили инициативу. </p><p align=\"center\">Если не получилось, напишите почему.</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Три дела, которые вы сделали хорошо. <br/>Почему вы сделали хорошо?</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Три дела, которые вы сделали плохо. <br/>Как можно было сделать хорошо? </p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Какую новую вещь вы сегодня сделали или<br/>какую старую сделали по-новому? </p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Удалось не заниматься работой после часа Х? </p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Физкультура сегодня была? </p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Медитировали?</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">За что вы сегодня были благодарны? </p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Сколько денег отправили на благотворительность? </p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Ловили себя на мысли, когда хотели сдаться?<br/>Что предприняли при этом? </p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Составьте список тех дел, которые вам нужно<br/>выполнить завтра:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Записать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())