from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget, QDialog
from Ui_service import Ui_Form_update, Ui_Dialog_delete
from database import Service, get_session


class ServiceDialog(QDialog, Ui_Dialog_delete):

    def __init__(self, text: str):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.selfText(text)





