from PyQt5 import QtWidgets
from FormLog import Ui_Dialog  # Importa la clase generada con el nombre correcto

class MainWindow(QtWidgets.QDialog, Ui_Dialog):  # Cambia Ui_MainWindow por Ui_Dialog
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Modifica el texto del label_3 como tenías en tu código original
        self.label.setText("Hola Soy Neftali")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
