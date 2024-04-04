import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from Service.service_table import ServiceTable
from Ui import Ui_Form_no_password
from Ui.ui_main_menu import Ui_Form_main_menu
from Ui.ui_menu import Ui_Form_menu
from Ui.ui_password import Ui_Form_password
from Ui.ui_usi_pochki import Ui_Form_pochki

# ошибки
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook

#Главное меню
class Main_menu(QWidget, Ui_Form_main_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_like_admin.clicked.connect(self.open_password)
    def open_password(self):
        self.window = Password()
        self.window.show()

#Окошко ввода пароля
class Password(QWidget, Ui_Form_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chek) #можно заходить и по кнопке
    def chek(self):
        if self.lineEdit.text() == "198687":
            self.window = Menu()
            self.window.show()
        else:
            self.window = No_Password()
            self.window.show()
            self.close()
        self.close()
    def keyPressEvent(self, event): #можно заходить жмякнув enter
        if event.key() == Qt.Key_Return:
            self.chek()

#Сообщение об ошибке
class No_Password(QWidget, Ui_Form_no_password):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)

#Меню выбора
class Menu(QWidget, Ui_Form_menu):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)
        self.push_button_service.clicked.connect(self.open_service)
        self.push_button_appointment.clicked.connect(self.open_appointment)
    def open_service(self):
        self.window = ServiceTable()
        self.window.show()
    def open_appointment(self):
        self.window = Usi_pochki()
        self.window.show()

class Usi_pochki(QWidget, Ui_Form_pochki):
    def __init__(self):  # просто появляется
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
ex_Main_menu = Main_menu()
ex_Main_menu.show()
sys.exit(app.exec_())