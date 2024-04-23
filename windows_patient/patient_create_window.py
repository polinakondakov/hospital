from typing import Iterable, Callable

from PyQt5.QtWidgets import QWidget

from database import get_session, Patient
from ui_patient import UiPatientCreateForm
# from ui.ui_patient_create import Ui_Form


class PatientCreate(QWidget, UiPatientCreateForm):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.pushButton_ok.clicked.connect(self.create_patient)
        self.pushButton_cancel.clicked.connect(lambda: self.close())

    def create_patient(self):
        full_name = self.line_edit_full_name.text()
        phone_number = self.line_edit_phone_number.text()
        sex = self.line_edit_sex.text()
        bdate = self.dateEdit.date().toPyDate()
        comments = self.line_edit_comments.text()
        new_patient = Patient(full_name=full_name,
                              phone_number=phone_number,
                              sex=sex,
                              bdate=bdate,
                              comments=comments)
        self.session.add(new_patient)
        self.session.commit()
        self.custom_close()


    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()
