from PyQt5 import QtWidgets
from FormMenu import Ui_FormMenu
from Encriptar import Encriptar
from Desencriptar import Desencriptar
from PyQt5.QtWidgets import QMessageBox

class Menu(QtWidgets.QMainWindow, Ui_FormMenu):
    def __init__(self, parent=None, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.parent = parent

        self.menuEncryptFile.addAction("Encriptar Archivo", self.openencriptar)
        self.menuDecrypt.addAction("Desencriptar Archivo", self.opendesencriptar)
        self.menuExit.addAction("Salir", self.salir)

    def openencriptar(self):
        opennewwindow = Encriptar(self)
        opennewwindow.show()

    def opendesencriptar(self):
        opennewwindow = Desencriptar(self)
        opennewwindow.show()

    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Deseas salir de la aplicación")
        msgBox.setWindowTitle("Cancelar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.hide()
            self.ocultar()

    def ocultar(self):
        if self.parent:
            self.parent.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMenu = Menu()
    FormMenu.show()
    sys.exit(app.exec_())