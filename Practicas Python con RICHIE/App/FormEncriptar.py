# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormEncriptar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SistemaEncriptar(object):
    def setupUi(self, SistemaEncriptar):
        SistemaEncriptar.setObjectName("SistemaEncriptar")
        SistemaEncriptar.resize(800, 726)
        self.centralwidget = QtWidgets.QWidget(SistemaEncriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 0, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Encriptar_6 = QtWidgets.QPushButton(self.tab)
        self.Encriptar_6.setGeometry(QtCore.QRect(600, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_6.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/candado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_6.setIcon(icon)
        self.Encriptar_6.setObjectName("Encriptar_6")
        self.Encriptar_3 = QtWidgets.QPushButton(self.tab)
        self.Encriptar_3.setGeometry(QtCore.QRect(600, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_3.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/cargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_3.setIcon(icon1)
        self.Encriptar_3.setObjectName("Encriptar_3")
        self.Encriptar_4 = QtWidgets.QPushButton(self.tab)
        self.Encriptar_4.setGeometry(QtCore.QRect(600, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_4.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/descargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_4.setIcon(icon2)
        self.Encriptar_4.setObjectName("Encriptar_4")
        self.Encriptar_5 = QtWidgets.QPushButton(self.tab)
        self.Encriptar_5.setGeometry(QtCore.QRect(600, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_5.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_5.setIcon(icon3)
        self.Encriptar_5.setObjectName("Encriptar_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 400, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.mensajeEncriptado = QtWidgets.QLabel(self.tab)
        self.mensajeEncriptado.setGeometry(QtCore.QRect(40, 440, 431, 131))
        self.mensajeEncriptado.setText("")
        self.mensajeEncriptado.setObjectName("mensajeEncriptado")
        self.Encriptar_7 = QtWidgets.QPushButton(self.tab)
        self.Encriptar_7.setGeometry(QtCore.QRect(600, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_7.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/enviar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_7.setIcon(icon4)
        self.Encriptar_7.setObjectName("Encriptar_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 581, 361))
        self.plainTextEdit.setObjectName("plainTextEdit")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../Encriptarqt/Encriptarqt/icon-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Encriptar_8 = QtWidgets.QPushButton(self.tab_2)
        self.Encriptar_8.setGeometry(QtCore.QRect(600, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_8.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/desencriptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Encriptar_8.setIcon(icon6)
        self.Encriptar_8.setObjectName("Encriptar_8")
        self.Encriptar_9 = QtWidgets.QPushButton(self.tab_2)
        self.Encriptar_9.setGeometry(QtCore.QRect(600, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_9.setFont(font)
        self.Encriptar_9.setIcon(icon3)
        self.Encriptar_9.setObjectName("Encriptar_9")
        self.Encriptar_10 = QtWidgets.QPushButton(self.tab_2)
        self.Encriptar_10.setGeometry(QtCore.QRect(600, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_10.setFont(font)
        self.Encriptar_10.setIcon(icon1)
        self.Encriptar_10.setObjectName("Encriptar_10")
        self.Encriptar_11 = QtWidgets.QPushButton(self.tab_2)
        self.Encriptar_11.setGeometry(QtCore.QRect(600, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_11.setFont(font)
        self.Encriptar_11.setIcon(icon2)
        self.Encriptar_11.setObjectName("Encriptar_11")
        self.Encriptar_12 = QtWidgets.QPushButton(self.tab_2)
        self.Encriptar_12.setGeometry(QtCore.QRect(600, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Encriptar_12.setFont(font)
        self.Encriptar_12.setIcon(icon4)
        self.Encriptar_12.setObjectName("Encriptar_12")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 50, 581, 501))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        SistemaEncriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SistemaEncriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SistemaEncriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SistemaEncriptar)
        self.statusbar.setObjectName("statusbar")
        SistemaEncriptar.setStatusBar(self.statusbar)

        self.retranslateUi(SistemaEncriptar)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SistemaEncriptar)

    def retranslateUi(self, SistemaEncriptar):
        _translate = QtCore.QCoreApplication.translate
        SistemaEncriptar.setWindowTitle(_translate("SistemaEncriptar", "MainWindow"))
        self.label.setText(_translate("SistemaEncriptar", "Mensaje:"))
        self.Encriptar_6.setText(_translate("SistemaEncriptar", "Encriptar"))
        self.Encriptar_3.setText(_translate("SistemaEncriptar", "Cargar"))
        self.Encriptar_4.setText(_translate("SistemaEncriptar", "Descargar"))
        self.Encriptar_5.setText(_translate("SistemaEncriptar", "Limpiar"))
        self.label_2.setText(_translate("SistemaEncriptar", "Mensaje Encriptado:"))
        self.Encriptar_7.setText(_translate("SistemaEncriptar", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SistemaEncriptar", "Encriptar texto"))
        self.label_3.setText(_translate("SistemaEncriptar", "Imagen:"))
        self.Encriptar_8.setText(_translate("SistemaEncriptar", "Desencriptar"))
        self.Encriptar_9.setText(_translate("SistemaEncriptar", "Limpiar"))
        self.Encriptar_10.setText(_translate("SistemaEncriptar", "Cargar"))
        self.Encriptar_11.setText(_translate("SistemaEncriptar", "Descargar"))
        self.Encriptar_12.setText(_translate("SistemaEncriptar", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SistemaEncriptar", "Encriptar Imagenes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SistemaEncriptar = QtWidgets.QMainWindow()
    ui = Ui_SistemaEncriptar()
    ui.setupUi(SistemaEncriptar)
    SistemaEncriptar.show()
    sys.exit(app.exec_())
