from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from FormLog import Ui_Dialog
from Menu import Menu


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Conecta los botones a los métodos correspondientes
        self.pushButton.clicked.connect(self.validar)
        self.pushButton_2.clicked.connect(self.cancelar)

    def validar(self):
        usuario = self.txtUser.text()  # Cambiado a txtUser
        contraseña = self.txtPassword.text()  # Cambiado a txtPassword
        if usuario == "admin" and contraseña == "1234":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Bienvenido al sistema")
            msgBox.setWindowTitle("Autorizado")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec_()
            if returnValue == QMessageBox.Ok:
                self.openwindow()
                self.hide()
            else:
                self.close()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Usuario o contraseña incorrectas")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def cancelar(self):
        self.close()

    def openwindow(self):
        openwindow = Menu(self)
        openwindow.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
