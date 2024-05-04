
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


class Cryptography:
    SECRET_KEY = b'TOPSECRETKEY_128'  # b'ThisIsA128BitKey'

    @staticmethod
    def encryption(text):
        cipher = AES.new(Cryptography.SECRET_KEY, AES.MODE_CBC)
        ciphertext_bytes = cipher.encrypt(
            pad(text.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
        return iv + ':' + ciphertext

    @staticmethod
    def decryption(encryptedText):
        if encryptedText == None:
            return encryptedText
        iv, ciphertext = encryptedText.split(':')
        iv = base64.b64decode(iv)
        ciphertext_bytes = base64.b64decode(ciphertext)
        cipher = AES.new(Cryptography.SECRET_KEY, AES.MODE_CBC, iv)
        plaintext_bytes = unpad(cipher.decrypt(
            ciphertext_bytes), AES.block_size)
        return plaintext_bytes.decode('utf-8')
