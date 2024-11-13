from PyQt5 import QtWidgets, QtGui
from FormLog import Ui_Dialog  # Importa la clase generada con el nombre correcto

class MainWindow(QtWidgets.QDialog, Ui_Dialog):  # Cambia Ui_MainWindow por Ui_Dialog
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Conecta los botones a los métodos correspondientes
        self.pushButton.clicked.connect(self.validar)
        self.pushButton_2.clicked.connect(self.cancelar)

    def validar(self):
        Usuario = self.lineEdit.text()
        Contraseña = self.lineEdit_3.text()
        if Usuario == "Nefta" and Contraseña == "1234":
            QtWidgets.QMessageBox.information(self, "Sesion iniciada correctamente", "Bienvenido "+Usuario)
        else:
            QtWidgets.QMessageBox.warning(self, "Logeo fallido", "Credenciales incorrectas")

    def cancelar(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()