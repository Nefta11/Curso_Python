from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FormMenu import Ui_FormMenu
from FormEncriptar import Ui_SistemaEncriptar


class Menu(QtWidgets.QMainWindow, Ui_FormMenu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_encrypt)
        self.pushButton2.clicked.connect(self.show_decrypt)
        self.menuHolala.addAction("Encriptar", self.show_encrypt)

    def show_encrypt(self):
        self.encrypt_window = Encrypt()
        self.encrypt_window.show()
        self.close()

    def show_decrypt(self):
        self.decrypt_window = Decrypt()
        self.decrypt_window.show()
        self.close()


class Encrypt(QtWidgets.QMainWindow, Ui_SistemaEncriptar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


class Decrypt(QtWidgets.QMainWindow, Ui_SistemaEncriptar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())
