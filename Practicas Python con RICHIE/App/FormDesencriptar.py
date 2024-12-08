# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormDesencriptar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SistemaDesencriptar(object):
    def setupUi(self, SistemaDesencriptar):
        SistemaDesencriptar.setObjectName("SistemaDesencriptar")
        SistemaDesencriptar.resize(811, 685)
        self.centralwidget = QtWidgets.QWidget(SistemaDesencriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.Desencriptar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Desencriptar_3.setGeometry(QtCore.QRect(600, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.Desencriptar_3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/cargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Desencriptar_3.setIcon(icon)
        self.Desencriptar_3.setObjectName("Desencriptar_3")
        self.Desencriptar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Desencriptar_4.setGeometry(QtCore.QRect(600, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.Desencriptar_4.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/descargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Desencriptar_4.setIcon(icon1)
        self.Desencriptar_4.setObjectName("Desencriptar_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 430, 261, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 571, 351))
        self.textEdit.setObjectName("textEdit")
        self.Desencriptar_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Desencriptar_5.setGeometry(QtCore.QRect(600, 120, 191, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.Desencriptar_5.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Desencriptar_5.setIcon(icon2)
        self.Desencriptar_5.setObjectName("Desencriptar_5")
        self.Encriptar_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Encriptar_6.setGeometry(QtCore.QRect(600, 60, 191, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.Encriptar_6.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/desencriptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_6.setIcon(icon3)
        self.Encriptar_6.setObjectName("Encriptar_6")
        SistemaDesencriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SistemaDesencriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 26))
        self.menubar.setObjectName("menubar")
        SistemaDesencriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SistemaDesencriptar)
        self.statusbar.setObjectName("statusbar")
        SistemaDesencriptar.setStatusBar(self.statusbar)

        self.retranslateUi(SistemaDesencriptar)
        QtCore.QMetaObject.connectSlotsByName(SistemaDesencriptar)

    def retranslateUi(self, SistemaDesencriptar):
        _translate = QtCore.QCoreApplication.translate
        SistemaDesencriptar.setWindowTitle(_translate("SistemaDesencriptar", "MainWindow"))
        self.Desencriptar_3.setText(_translate("SistemaDesencriptar", "Cargar Archivo"))
        self.Desencriptar_4.setText(_translate("SistemaDesencriptar", "Guardar Archivo"))
        self.label.setText(_translate("SistemaDesencriptar", "Mensaje:"))
        self.label_2.setText(_translate("SistemaDesencriptar", "Mensaje Encriptado:"))
        self.Desencriptar_5.setText(_translate("SistemaDesencriptar", "Limpiar"))
        self.Encriptar_6.setText(_translate("SistemaDesencriptar", "Desencriptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SistemaDesencriptar = QtWidgets.QMainWindow()
    ui = Ui_SistemaDesencriptar()
    ui.setupUi(SistemaDesencriptar)
    SistemaDesencriptar.show()
    sys.exit(app.exec_())