# FORMMENU.PY
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormMenu(object):
    def setupUi(self, FormMenu):
        FormMenu.setObjectName("FormMenu")
        FormMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FormMenu)
        self.centralwidget.setObjectName("centralwidget")

        # Añadir etiqueta de bienvenida
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QtCore.QRect(200, 50, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_welcome.setFont(font)
        self.label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_welcome.setObjectName("label_welcome")

        # Añadir espacio para la imagen
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(200, 110, 400, 200))
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")

        # Añadir etiqueta de pregunta
        self.label_question = QtWidgets.QLabel(self.centralwidget)
        self.label_question.setGeometry(QtCore.QRect(200, 320, 400, 50))
        font.setPointSize(16)
        self.label_question.setFont(font)
        self.label_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question.setObjectName("label_question")

        FormMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FormMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuEncryptFile = QtWidgets.QMenu(self.menubar)
        self.menuEncryptFile.setObjectName("menuEncryptFile")
        self.menuDecrypt = QtWidgets.QMenu(self.menubar)
        self.menuDecrypt.setObjectName("menuDecrypt")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        FormMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FormMenu)
        self.statusbar.setObjectName("statusbar")
        FormMenu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEncryptFile.menuAction())
        self.menubar.addAction(self.menuDecrypt.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(FormMenu)
        QtCore.QMetaObject.connectSlotsByName(FormMenu)

    def retranslateUi(self, FormMenu):
        _translate = QtCore.QCoreApplication.translate
        FormMenu.setWindowTitle(_translate("FormMenu", "MainWindow"))
        self.label_welcome.setText(_translate("FormMenu", "Bienvenido al sistema SIUU"))
        self.label_image.setText(_translate("FormMenu", ""))  # Aquí puedes añadir un texto o dejarlo vacío para la imagen
        self.label_question.setText(_translate("FormMenu", "¿Qué desea realizar, amigazo?"))
        self.menuEncryptFile.setTitle(_translate("FormMenu", "Encriptar Archivo"))
        self.menuDecrypt.setTitle(_translate("FormMenu", "Desencriptar"))
        self.menuHelp.setTitle(_translate("FormMenu", "Ayuda"))
        self.menuExit.setTitle(_translate("FormMenu", "Salir"))

        # Establecer la imagen
        self.label_image.setPixmap(QtGui.QPixmap("../App/images/encriptar _ desencriptar UTXJ sIU.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMenu = QtWidgets.QMainWindow()
    ui = Ui_FormMenu()
    ui.setupUi(FormMenu)
    FormMenu.show()
    sys.exit(app.exec_())