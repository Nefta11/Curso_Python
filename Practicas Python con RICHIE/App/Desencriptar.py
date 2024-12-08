from FormEncriptar  import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from datetime import *
import smtplib 
from email.message import EmailMessage 

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnEncriptar.clicked.connect(self.encrypt_data_AES)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnDescargar.clicked.connect(self.crearFichero)
        self.btnCargar.clicked.connect(self.uploadFichero)
        self.btnEnviar.clicked.connect(self.eviarCorreo)
    
    def encrypt_data_AES(self):
        data = self.textMensaje.toPlainText()
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
        self.textMensaje.clear()
        self.lblMensajeEncriptado.clear()
    
    def crearFichero(self):
        cadena=self.lblMensajeEncriptado.text()
        cadenaencriptada = self.lblMensaje.text()
        if cadena!="" and cadenaencriptada!="":
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
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*.txt);;Python Files (*.py)", options=options)
        #fileName, _ =QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if fileName:
            with open(fileName, 'r') as fichero:
                mensaje = fichero.read()
            self.textMensaje.setText(mensaje)
    
    def eviarCorreo(self):
        email_subject = "Datos encriptados" 
        sender_email_address = "neftaliarturohernandez@gmail.com" 
        receiver_email_address = "220100@utxicotepec.edu.mx\Ó" 
        email_smtp = "smtp-mail.outlook.com" 
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