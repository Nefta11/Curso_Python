from PyQt5 import QtWidgets
from FormLog import Ui_Dialog  # Importa la clase generada con el nombre correcto

class MainWindow(QtWidgets.QDialog, Ui_Dialog):  # Cambia Ui_MainWindow por Ui_Dialog
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Conecta el botón al método validar
        self.pushButton.clicked.connect(self.validar)

    def validar(self):
        Usuario = self.lineEdit.text()
        Contraseña = self.lineEdit_3.text()
        if Usuario == "Administrador" and Contraseña == "123":
            print("Welcome to the system")
        else:
            print("Invalid credentials")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()