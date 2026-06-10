import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.pushDecrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self,text):
        key = self.ui.textKey.toPlainText().strip()
        if not key.isdigit():
            QMessageBox.warning(self,"Khóa không hợp lệ","Khóa phải là số nguyên.")
            return False
        
        key = int(key)
        if key <= 1:
            QMessageBox.warning(self,"Khóa không hợp lệ","Khóa phải lớn hơn 1.")
            return False
        
        if int(key) >= len(text):
            QMessageBox.warning(self,"Khóa không hợp lệ","Khóa phải nhỏ hơn độ dài văn bản.")
            return False
        

        return True

    def call_api_encrypt(self):
        if not self.validate_key(self.ui.textPlainText.toPlainText()):
            return
        
        plaintext = self.ui.textPlainText.toPlainText().strip()
        if not plaintext:
            QMessageBox.warning(self,"Lỗi","Plaintext không được để trống.")
            return

        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.textPlainText.toPlainText(),
            "key": self.ui.textKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textCipherText.setText(data["encrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_decrypt(self):
        if not self.validate_key(self.ui.textCipherText.toPlainText()):
            return
        
        ciphertext = self.ui.textCipherText.toPlainText().strip()
        if not ciphertext:
            QMessageBox.warning(self,"Lỗi","Ciphertext không được để trống.")
            return

        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.textCipherText.toPlainText(),
            "key": self.ui.textKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textPlainText.setText(data["decrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
