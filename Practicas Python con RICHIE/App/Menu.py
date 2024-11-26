from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FormMenu import Ui_FormMenu

from Encriptar import *
from Desencriptar import *

class Menu(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.openEncriptar)
        self.pushButton2.clicked.connect(self.openDesencriptar)

        self.menuEncriptar.addAction("Encriptar", self.openEncriptar) 

    def openEncriptar(self):
        openwwindow = Encriptar(self)
        openwwindow.show()
    
    def openDesencriptar(self):
        openwwindow = Desencriptar(self)
        openwwindow.show()