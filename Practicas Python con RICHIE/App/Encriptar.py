from PyQt5 import QtWidgets
from FormEncriptar import Ui_FrmEncriptar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwargs):
        super(Encriptar, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encrypt_data_AES)
        self.btnLimpiar.clicked.connect(self.limpiar)

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
        self.lblMensajeEncriptado.clear()
        self.txtMensaje.clear()