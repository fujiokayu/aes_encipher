from Crypto.Cipher import AES
from base64 import b64encode


class AesEncipher:
    def __init__(self, mode, key):
        self.key = key
        self.mode = mode

    def encrypt(self, data): 
        self.cipher = AES.new(self.key, self.mode)
        return self.cipher.encrypt(data)
        
    def decrypt(self, data, nonce):
        self.cipher = AES.new(self.key, self.mode, nonce = nonce)
        return self.cipher.decrypt(data)

    def get_nonce(self):
        return b64encode(self.cipher.nonce).decode('utf-8')

    def get_key(self):
        return b64encode(self.key).decode('utf-8')
