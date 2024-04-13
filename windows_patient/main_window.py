from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from database import Patient, get_session
#from main import PatientCreate
from ui_patient import UiMainWindow

from windows_patient.patient_create_window import PatientCreate
from windows_patient.patient_dialog import PatientDialog
from windows_patient.patient_update_window import PatientUpdate

class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.current_row = None

        self.push_button_create.clicked.connect(self.open_patient_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_patient_update)
        self.push_button_delete.clicked.connect(self.open_dialog_delete_patient)
        self.tableWidget.cellClicked.connect(self.table_widget_cell_clicked)

        self.updateTable()




    def updateTable(self):
        patientss = self.session.query(Patient).order_by(Patient.id).all()
        self.tableWidget.setRowCount(0)
        for patient in patientss:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(patient.id)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(patient.full_name))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(patient.phone_number)))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(patient.sex))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(patient.bdate)))

    def table_widget_cell_clicked(self, row, column):
        self.current_row = row


    def open_patient_create(self):
        self.create_window = PatientCreate([self.updateTable])
        self.create_window.show()

    def open_patient_update(self, row, column):
        patient_id = int(self.tableWidget.item(row, 0).text())
        patient = self.session.query(Patient).get(patient_id)
        self.create_window = PatientUpdate(patient, [self.updateTable])
        self.create_window.show()


    def open_dialog_delete_patient(self):
        if self.current_row is None:
            return
        dialog_delete = PatientDialog("Точно хотите удалить???")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            patient_id = int(self.tableWidget.item(self.current_row, 0).text())
            patient = self.session.query(Patient).get(patient_id)
            self.session.delete(patient)
            self.session.commit()
            self.updateTable()

