from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from Appointment.app_create import AppCreate
from Appointment.app_update import AppUpdate
from Appointment.dialog_app import Dialog_service
from Ui_app import Ui_Appointment_table
from database import get_session, Appointment


class AppTable(QMainWindow, Ui_Appointment_table):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.current_row = None
        self.push_button_app_create.clicked.connect(self.open_app_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_app_update)
        self.push_button_service_delete.clicked.connect(self.open_dialog_delete_app)
        self.tableWidget.cellClicked.connect(self.table_widget_cell_clicked)

        self.update_table()

    def update_table(self):
        appointments = self.session.query(Appointment).order_by(Appointment.id).all()
        self.tableWidget.setRowCount(0)
        for appointment in appointments:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(appointment.id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(appointment.doctor_id)))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(appointment.patient_id)))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(appointment.office_number)))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(appointment.date_and_time)))

    def table_widget_cell_clicked(self, row, column):
        self.current_row = row


    def open_app_create(self):
        self.create_window = AppCreate([self.update_table])
        self.create_window.show()

    def open_app_update(self, row, column):
        appointment_id = int(self.tableWidget.item(row, 0).text())
        appointment = self.session.query(Appointment).get(appointment_id)
        self.create_window = AppUpdate(appointment, [self.update_table])
        self.create_window.show()

    def open_dialog_delete_app(self):
        if self.current_row is None:
            return
        dialog_delete = Dialog_service("Точно хотите удалить??")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            appointment_id = int(self.tableWidget.item(self.current_row, 0).text())
            appointment = self.session.query(Appointment).get(appointment_id)
            self.session.delete(appointment)
            self.session.commit()
            self.update_table()