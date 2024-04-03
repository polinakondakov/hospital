import sys
from datetime import time

from PyQt5.QtWidgets import QWidget, QApplication
from Service.service_table import ServiceTable
from Ui import Ui_Form_no_password
from Ui.ui_chek_admin import Ui_Form_chek_admin
from Ui.ui_glav_menu import Ui_Form_glav_menu
from Ui.ui_menu import Ui_Form_menu
from Ui.ui_password import Ui_Form_password
from Ui.ui_usi_pochki import Ui_Form_pochki

from database import get_session, Service

sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook

class Glavnoe_menu(QWidget, Ui_Form_glav_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        #self.push_button_like_admin.clicked.connect(self.open_chek_admin)
        self.push_button_like_admin.clicked.connect(self.open_password)
    #def open_chek_admin(self):
        #self.window = Chek_admin()
       # self.window.show()

    def open_password(self):
        self.window = Password()
        self.window.show()

class Password(QWidget, Ui_Form_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chek)

    def chek(self):
        if self.lineEdit.text() == "198687":
            self.window = Menu()
            self.window.show()
        else:
            self.window = No_Password()
            self.window.show()
            self.close()
        self.close()

class No_Password(QWidget, Ui_Form_no_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
class Chek_admin(QWidget, Ui_Form_chek_admin):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_yes.clicked.connect(self.lie)
        self.push_button_no.clicked.connect(self.lie)
        self.push_button_vran.clicked.connect(self.lie)
        self.push_button_right.clicked.connect(self.open_menu)
    def lie(self):
        all.close()
    def open_menu(self):
        self.window = Menu()
        self.window.show()
class Menu(QWidget, Ui_Form_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_service.clicked.connect(self.open_service) #когда нажимаешл на push_button_service открываются услуги

    def open_service(self):
        self.window = ServiceTable()
        self.window.show()

class UsiPochki(QWidget, Ui_Form_pochki):
    def __init__(self):  #просто появляется
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex_menu = Glavnoe_menu()
ex_menu.show()
#ex = ServiceTable()
#ex.show()
#ex_pochki = UsiPochki()
#ex_pochki.show()
sys.exit(app.exec_())