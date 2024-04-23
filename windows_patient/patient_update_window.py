from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget

from database import get_session, Patient
from ui_patient import UiPatientUpdateForm
# from ui.ui_patient_create import Ui_Form


class PatientUpdate(QWidget, UiPatientUpdateForm):
    def __init__(self, patient: Patient, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.pushButton_ok.clicked.connect(self.update_patient)
        self.pushButton_cancel.clicked.connect(lambda: self.close())

        self.label_id.setText(str(patient.id))
        self.line_edit_full_name.setText(patient.full_name)
        self.line_edit_phone_number.setText(str(patient.phone_number))
        self.line_edit_sex.setText(str(patient.sex))
        self.line_edit_comments.setText(str(patient.comments))
        self.dateEdit.setDate(QDate.fromString(str(patient.bdate)))


    def update_patient(self):
        full_name = self.line_edit_full_name.text()
        phone_number = self.line_edit_phone_number.text()
        sex = self.line_edit_sex.text()
        bdate = self.dateEdit.date().toPyDate()
        patient_id = int(self.label_id.text())
        comments = self.line_edit_comments.text()

        exit_patient: Patient = self.session.query(Patient).get(patient_id)
        exit_patient.full_name = full_name
        exit_patient.phone_number = phone_number
        exit_patient.sex = sex
        exit_patient.comments = comments
        exit_patient.bdate = bdate
        self.session.commit()
        self.custom_close()


    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()

