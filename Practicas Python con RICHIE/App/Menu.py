from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FormMenu import Ui_FormMenu  # Cambiado a Ui_FormMenu

class Menu(QtWidgets.QDialog, Ui_FormMenu):  # Cambiado a Ui_FormMenu
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def show_message(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Información")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())