from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget
from Ui_app import Ui_Appointment_update
from database import get_session, Appointment


class AppUpdate(QWidget, Ui_Appointment_update):

    def __init__(self, appointment: Appointment, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_button_save.clicked.connect(self.update_app)
        self.push_button_undo.clicked.connect(lambda: self.close())


        self.label_id.setText(str(appointment.id))
        self.line_edit_patient_id.setText(str(appointment.patient_id))
        self.line_edit_doctor_id.setText(str(appointment.doctor_id))
        self.line_edit_number_room.setText(str(appointment.office_number))
        self.line_edit_date_and_time.setText(str(appointment.date_and_time))

    def update_app(self):
        patient_id = self.line_edit_patient_id.text()
        doctor_id = self.line_edit_doctor_id.text()
        office_number = self.line_edit_number_room.text()
        date_and_time = self.line_edit_date_and_time.text()
        appointment_id = int(self.label_id.text())
        exist_appointment: Appointment = self.session.query(Appointment).get(appointment_id)
        exist_appointment.patient_id = patient_id
        exist_appointment.doctor_id = doctor_id
        exist_appointment.office_number = office_number
        exist_appointment.date_and_time = date_and_time
        self.session.commit()
        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()