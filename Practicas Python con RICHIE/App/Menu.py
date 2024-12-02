# MENU.PY
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FormMenu import Ui_FormMenu
from FormEncriptar import Ui_SistemaEncriptar
from FormLog import Ui_Dialog


class Menu(QtWidgets.QMainWindow, Ui_FormMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionEncrypt.triggered.connect(self.show_encrypt)
        self.actionDecrypt.triggered.connect(self.show_decrypt)
        self.actionExit.triggered.connect(self.close_application)

    def show_encrypt(self):
        self.encrypt_window = Encrypt()
        self.encrypt_window.show()
        self.close()

    def show_decrypt(self):
        self.decrypt_window = Encrypt()
        self.decrypt_window.tabWidget.setCurrentIndex(1)
        self.decrypt_window.show()
        self.close()

    def close_application(self):
        reply = QMessageBox.question(
            self,
            "Confirmar salida",
            "¿Está seguro de que desea salir?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.show_login()
        else:
            pass

    def show_login(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()


class Encrypt(QtWidgets.QMainWindow, Ui_SistemaEncriptar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


class Login(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
