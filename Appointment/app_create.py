from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Ui_app import Ui_Appointment_create
from database import Appointment, get_session

class AppCreate(QWidget, Ui_Appointment_create):

    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save.clicked.connect(self.create_app)
        self.push_button_undo.clicked.connect(lambda: self.close())

    def create_app(self):
        id = self.lineEdit.text()
        patient_id = self.line_edit_patient_id.text()
        doctor_id = self.line_edit_doctor_id.text()
        office_number = self.line_edit_number_room.text()
        date_and_time = self.line_edit_date_and_time.text()
        new_app = Appointment(id = id,
                              patient_id = patient_id,
                              doctor_id=doctor_id,
                              office_number= office_number,
                              date_and_time=date_and_time)
        self.session.add(new_app)
        self.session.commit()

        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()