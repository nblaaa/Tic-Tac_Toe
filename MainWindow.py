# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(10, 50, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button1.setFont(font)
        self.Button1.setText("")
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(140, 50, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button2.setFont(font)
        self.Button2.setText("")
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(270, 50, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button3.setFont(font)
        self.Button3.setText("")
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(10, 180, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button4.setFont(font)
        self.Button4.setText("")
        self.Button4.setObjectName("Button4")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(10, 310, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button7.setFont(font)
        self.Button7.setText("")
        self.Button7.setObjectName("Button7")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(140, 180, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button5.setFont(font)
        self.Button5.setText("")
        self.Button5.setObjectName("Button5")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(270, 180, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button6.setFont(font)
        self.Button6.setText("")
        self.Button6.setObjectName("Button6")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(140, 310, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button8.setFont(font)
        self.Button8.setText("")
        self.Button8.setObjectName("Button8")
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setEnabled(True)
        self.Button9.setGeometry(QtCore.QRect(270, 310, 120, 120))
        font = QtGui.QFont()
        font.setPointSize(99)
        self.Button9.setFont(font)
        self.Button9.setText("")
        self.Button9.setObjectName("Button9")
        self.NewGame = QtWidgets.QPushButton(self.centralwidget)
        self.NewGame.setGeometry(QtCore.QRect(10, 440, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.NewGame.setFont(font)
        self.NewGame.setObjectName("NewGame")
        self.About = QtWidgets.QPushButton(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(10, 500, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.About.setFont(font)
        self.About.setObjectName("About")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(10, 560, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 381, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(23)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Крестики-Нолики"))
        self.NewGame.setText(_translate("MainWindow", "Новая игра"))
        self.About.setText(_translate("MainWindow", "О программе"))
        self.Exit.setText(_translate("MainWindow", "Выход"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Хотите сыграть?</span></p></body></html>"))
