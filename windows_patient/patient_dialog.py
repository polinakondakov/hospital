from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog

from database import get_session, Patient
from ui_patient import UiDialog




class PatientDialog(QDialog, UiDialog):
    def __init__(self, text: str):
        super().__init__()
        self.setupUi(self)
        self.session = get_session()

        self.textBrowser.setText(text)


    def accept(self):
        super().accept()



