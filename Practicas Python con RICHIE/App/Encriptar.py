from FormEncriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PyQt5.QtWidgets import QFileDialog  # type: ignore

class Encriptar(QtWidgets.QMainWindow, Ui_SistemaEncriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.Encriptar_6.clicked.connect(self.encriptarAES)
        self.Encriptar_5.clicked.connect(self.limpiarCampos)
        self.Encriptar_3.clicked.connect(self.cargarArchivo)
        self.Encriptar_4.clicked.connect(self.guardarArchivo)  

    def encriptarAES(self):
        data = self.textEdit.toPlainText()
        if not data:
            self.mensajeEncriptado.setText("Por favor, introduce un texto o carga un archivo.")
            return

        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        try:
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(data.encode('utf-8'))
            padded_data += padder.finalize()

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()

            self.mensajeEncriptado.setText(f'{ciphertext}')
        except Exception as e:
            self.mensajeEncriptado.setText(f"Error al encriptar: {e}")

    def limpiarCampos(self):
        self.textEdit.clear()
        self.mensajeEncriptado.clear()

    def cargarArchivo(self):
        options = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*)", options=options)

        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as file:
                    contenido = file.read()
                    self.textEdit.setText(contenido) 
                    self.encriptarAES() 
            except Exception as e:
                self.textEdit.setText(f"Error al leer el archivo: {e}")

    def guardarArchivo(self):
        options = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=options)

        if archivo:
            try:
                texto_encriptado = self.mensajeEncriptado.text()
                if not texto_encriptado:
                    self.mensajeEncriptado.setText("No hay texto encriptado para guardar.")
                    return

                with open(archivo, 'w', encoding='utf-8') as file:
                    file.write(texto_encriptado)
            except Exception as e:
                self.mensajeEncriptado.setText(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Encriptar()
    window.show()
    sys.exit(app.exec_())