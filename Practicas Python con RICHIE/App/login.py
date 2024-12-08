from PyQt5 import QtWidgets
from FormLog import Ui_Dialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.validar)
        self.pushButton_2.clicked.connect(self.salir)
        self.menu_window = None  # Añadir una referencia para la ventana del menú

        # Configurar el campo de contraseña para que no se vea mientras se teclea
        self.txtPassword.setEchoMode(QLineEdit.Password)

    def validar(self):
        usuario = self.txtUser.text()
        constrasena = self.txtPassword.text()
        if usuario == "admin" and constrasena == "1234":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Bienvenido al sistema")
            msgBox.setWindowTitle("Autorizado")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.openwindow()
                self.close()  
            else:
                self.close()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Error usuario o contraseña incorrectos")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Deseas salir de la aplicación")
        msgBox.setWindowTitle("Cancelar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.close()

    def openwindow(self):
        from Menu import Menu  
        self.menu_window = Menu(self) 
        self.menu_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()