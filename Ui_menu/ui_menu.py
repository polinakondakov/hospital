# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 377)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setStyleSheet("")
        self.push_button_appointment = QtWidgets.QPushButton(Form)
        self.push_button_appointment.setGeometry(QtCore.QRect(130, 150, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_appointment.setFont(font)
        self.push_button_appointment.setStyleSheet("")
        self.push_button_appointment.setObjectName("push_button_appointment")
        self.push_button_patient = QtWidgets.QPushButton(Form)
        self.push_button_patient.setEnabled(True)
        self.push_button_patient.setGeometry(QtCore.QRect(130, 290, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_patient.setFont(font)
        self.push_button_patient.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.push_button_patient.setAcceptDrops(False)
        self.push_button_patient.setStyleSheet("")
        self.push_button_patient.setObjectName("push_button_patient")
        self.pushButton_doctor = QtWidgets.QPushButton(Form)
        self.pushButton_doctor.setGeometry(QtCore.QRect(130, 220, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_doctor.setFont(font)
        self.pushButton_doctor.setStyleSheet("")
        self.pushButton_doctor.setObjectName("pushButton_doctor")
        self.push_button_service = QtWidgets.QPushButton(Form)
        self.push_button_service.setGeometry(QtCore.QRect(130, 80, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_service.setFont(font)
        self.push_button_service.setMouseTracking(True)
        self.push_button_service.setFocusPolicy(QtCore.Qt.TabFocus)
        self.push_button_service.setStyleSheet("")
        self.push_button_service.setObjectName("push_button_service")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 20, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -55, 731, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/основной фон.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.push_button_appointment.raise_()
        self.push_button_patient.raise_()
        self.pushButton_doctor.raise_()
        self.push_button_service.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.push_button_appointment.setText(_translate("Form", "ЗАПИСЬ НА ПРИЕМ"))
        self.push_button_patient.setText(_translate("Form", "ПАЦИЕНТЫ"))
        self.pushButton_doctor.setText(_translate("Form", "ВРАЧИ"))
        self.push_button_service.setText(_translate("Form", "УСЛУГИ"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Выберите необходимую таблицу, для внесения изменений</span></p></body></html>"))
