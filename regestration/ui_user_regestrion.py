# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_regestration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_user_regestration(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 719)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 511, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/фон регистрации.png"))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(-60, 10, 581, 51))
        self.textBrowser.setStyleSheet("Войдите или зарегистрируйтесь!")
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.push_button_registration_reg = QtWidgets.QPushButton(Form)
        self.push_button_registration_reg.setGeometry(QtCore.QRect(130, 650, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_registration_reg.setFont(font)
        self.push_button_registration_reg.setObjectName("push_button_registration_reg")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.line_edit_fio_reg = QtWidgets.QLineEdit(Form)
        self.line_edit_fio_reg.setGeometry(QtCore.QRect(10, 120, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_fio_reg.setFont(font)
        self.line_edit_fio_reg.setObjectName("line_edit_fio_reg")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.line_edit_phone_reg = QtWidgets.QLineEdit(Form)
        self.line_edit_phone_reg.setGeometry(QtCore.QRect(10, 220, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_phone_reg.setFont(font)
        self.line_edit_phone_reg.setObjectName("line_edit_phone_reg")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.line_edit_sex_reg = QtWidgets.QLineEdit(Form)
        self.line_edit_sex_reg.setGeometry(QtCore.QRect(10, 310, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_sex_reg.setFont(font)
        self.line_edit_sex_reg.setObjectName("line_edit_sex_reg")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.date_edit_bdate_reg = QtWidgets.QDateEdit(Form)
        self.date_edit_bdate_reg.setGeometry(QtCore.QRect(10, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_edit_bdate_reg.setFont(font)
        self.date_edit_bdate_reg.setObjectName("date_edit_bdate_reg")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 540, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.line_edit_sex_reg_2 = QtWidgets.QLineEdit(Form)
        self.line_edit_sex_reg_2.setGeometry(QtCore.QRect(10, 500, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_edit_sex_reg_2.setFont(font)
        self.line_edit_sex_reg_2.setObjectName("line_edit_sex_reg_2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 440, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.push_button_registration_reg_2 = QtWidgets.QPushButton(Form)
        self.push_button_registration_reg_2.setGeometry(QtCore.QRect(100, 580, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_button_registration_reg_2.setFont(font)
        self.push_button_registration_reg_2.setObjectName("push_button_registration_reg_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Оставить заявку на запись</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.push_button_registration_reg.setText(_translate("Form", "Оставить заявку"))
        self.label_3.setText(_translate("Form", "Введите ФИО*:"))
        self.label_5.setText(_translate("Form", "Введите дату рождения:"))
        self.label_6.setText(_translate("Form", "Введите номер телефона*:"))
        self.label_7.setText(_translate("Form", "Укажите ваш пол:"))
        self.label_8.setText(_translate("Form", "* - поле является обязательным для заполнения"))
        self.label_9.setText(_translate("Form", "Укажите желаемую услугу:"))
        self.push_button_registration_reg_2.setText(_translate("Form", "Услуги"))
