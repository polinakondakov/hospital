# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service_create.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_service(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 319)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_edit_price = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_price.setObjectName("line_edit_price")
        self.gridLayout_2.addWidget(self.line_edit_price, 2, 1, 1, 1)
        self.line_edit_doctor_id = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_doctor_id.setObjectName("line_edit_doctor_id")
        self.gridLayout_2.addWidget(self.line_edit_doctor_id, 0, 1, 1, 1)
        self.line_edit_title = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_title.setObjectName("line_edit_title")
        self.gridLayout_2.addWidget(self.line_edit_title, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.push_button_undo = QtWidgets.QPushButton(self.groupBox)
        self.push_button_undo.setObjectName("push_button_undo")
        self.gridLayout_2.addWidget(self.push_button_undo, 3, 0, 1, 1)
        self.push_button_save = QtWidgets.QPushButton(self.groupBox)
        self.push_button_save.setObjectName("push_button_save")
        self.gridLayout_2.addWidget(self.push_button_save, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Добавить услугу"))
        self.label_2.setText(_translate("Form", "Название услуги"))
        self.label.setText(_translate("Form", "     id врача     "))
        self.label_3.setText(_translate("Form", "        Цена"))
        self.push_button_undo.setText(_translate("Form", "Отмена"))
        self.push_button_save.setText(_translate("Form", "Сохранить"))
