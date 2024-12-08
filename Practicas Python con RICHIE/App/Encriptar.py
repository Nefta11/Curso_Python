from FormEncriptar import Ui_FrmEncriptar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QMainWindow, QApplication
from PyQt5 import QtGui
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

class Encriptar(QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwargs):
        super(Encriptar, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnEncriptar.clicked.connect(self.encrypt_data_AES)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnCargar.clicked.connect(self.uploadFichero)
        self.btnDescargar.clicked.connect(self.crearFichero)
        self.btnEncriptar_2.clicked.connect(self.encrypt_image_AES)
        self.btnLimpiar_2.clicked.connect(self.limpiar_imagen)
        self.btnCargar_2.clicked.connect(self.upload_imagen)
        self.btnDescargar_2.clicked.connect(self.crearFichero_imagen)
    
    def encrypt_data_AES(self):
        data = self.txtMensaje.toPlainText()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode('utf-8'))
        padded_data += padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        self.lblMensajeEncriptado.setText(f'{ciphertext}')
    
    def limpiar(self):
        self.txtMensaje.clear()
        self.lblMensajeEncriptado.clear()
    
    def crearFichero(self):
        cadena = self.lblMensajeEncriptado.text()
        if cadena != "":
            fecha = datetime.now()
            d = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f'archivosEnc/MensajeEnc-{d}.txt', 'w') as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos guardados correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay texto encriptado que almacenar")
    
    def uploadFichero(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*.txt);;Python Files (*.py)", options=options)
        if fileName:
            with open(fileName, 'r') as fichero:
                mensaje = fichero.read()
            self.txtMensaje.setText(mensaje)
    
    def enviarCorreo(self):
        email_subject = "Datos encriptados"
        sender_email_address = "neftaliarturohernandez@gmail.com"
        receiver_email_address = "220100a@utxicotepec.edu.mx"
        email_smtp = "smtp.gmail.com"
        email_password = "7641146446"

        # Create an email message object
        message = EmailMessage()

        # Configure email headers
        message['Subject'] = email_subject
        message['From'] = sender_email_address
        message['To'] = receiver_email_address

        # Set email body text
        message.set_content(self.lblMensajeEncriptado.text())

        # Set smtp server and port
        server = smtplib.SMTP(email_smtp, '587')

        # Identify this client to the SMTP server
        server.ehlo()

        # Secure the SMTP connection
        server.starttls()

        # Login to email account
        server.login(sender_email_address, email_password)

        # Send email
        server.send_message(message)

        # Close connection to server
        server.quit()

    def encrypt_image_AES(self):
        if hasattr(self, 'image_path'):
            with open(self.image_path, 'rb') as image_file:
                image_data = image_file.read()
            key = b"123456789101112131415161718_UTXJ"
            iv = b"TI_UTXJ2024ENCRI"
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(image_data)
            padded_data += padder.finalize()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            self.label.setText(f'{ciphertext}')
    
    def limpiar_imagen(self):
        self.label.clear()
    
    def crearFichero_imagen(self):
        cadena = self.label.text()
        if cadena != "":
            fecha = datetime.now()
            d = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f'archivosEnc/ImagenEnc-{d}.txt', 'w') as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos guardados correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay imagen encriptada que almacenar")
    
    def upload_imagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*.jpg *.png *.bmp);;Python Files (*.py)", options=options)
        if fileName:
            self.label.setPixmap(QtGui.QPixmap(fileName))
            self.image_path = fileName  # Guardar la ruta del archivo de imagen

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    FrmEncriptar = QMainWindow()
    ui = Encriptar()
    ui.setupUi(FrmEncriptar)
    FrmEncriptar.show()
    sys.exit(app.exec_())