from FormDesencriptar import Ui_SistemaDesencriptar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os


class Desencriptar(QtWidgets.QMainWindow, Ui_SistemaDesencriptar):
    def __init__(self, *args, **kwargs):
        super(Desencriptar, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Encriptar_6.clicked.connect(self.desencrypt_data_AES)
        self.Desencriptar_5.clicked.connect(self.limpiar)
        self.Desencriptar_4.clicked.connect(self.crearFichero)
        self.Desencriptar_3.clicked.connect(self.uploadFichero)

    def desencrypt_data_AES(self):
        data = self.textEdit.toPlainText()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"
        cadena_bytes = eval(data)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        # Desencriptar los datos
        mensaje_desencriptado = decryptor.update(cadena_bytes) + decryptor.finalize()
        # El mensaje desencriptado puede contener padding, así que lo eliminamos
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        mensaje_desencriptado = (
            unpadder.update(mensaje_desencriptado) + unpadder.finalize()
        )

        try:
            # Intentar decodificar como texto
            texto_desencriptado = mensaje_desencriptado.decode("utf-8")
            self.textEdit.setText(texto_desencriptado)
        except UnicodeDecodeError:
            # Si falla, asumir que es una imagen
            self.textEdit.clear()
            self.label.setPixmap(QtGui.QPixmap())
            self.label.setText("Imagen desencriptada")
            with open("imagen_desencriptada.jpg", "wb") as image_file:
                image_file.write(mensaje_desencriptado)
            self.label.setPixmap(QtGui.QPixmap("imagen_desencriptada.jpg"))

    def limpiar(self):
        self.textEdit.clear()
        self.label.clear()

    def crearFichero(self):
        cadena = self.textEdit.toPlainText()
        if cadena != "":
            fecha = datetime.now()
            d = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f"archivosDes/MensajeDes-{d}.txt", "w") as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos guardados correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay texto desencriptado que almacenar")

    def uploadFichero(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*.txt);;Python Files (*.py)",
            options=options,
        )
        if fileName:
            with open(fileName, "r") as fichero:
                mensaje = fichero.read()
            self.textEdit.setText(mensaje)

    def enviarCorreo(self):
        email_subject = "Datos desencriptados"
        sender_email_address = "neftaliarturohernandez@gmail.com"
        receiver_email_address = "220100a@utxicotepec.edu.mx"
        email_smtp = "smtp.gmail.com"
        email_password = "7641146446"

        # Create an email message object
        message = EmailMessage()

        # Configure email headers
        message["Subject"] = email_subject
        message["From"] = sender_email_address
        message["To"] = receiver_email_address

        # Set email body text
        message.set_content(self.textEdit.toPlainText())

        # Set smtp server and port
        server = smtplib.SMTP(email_smtp, "587")

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Desencriptar()
    window.show()
    sys.exit(app.exec_())
