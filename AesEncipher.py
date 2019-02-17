from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode


class AesEncipher:
    def __init__(self, mode, key, encoded_nonce = ""):
        self.key = key
        self.mode = mode
        if len(encoded_nonce) == 0:
            self.cipher = AES.new(self.key, self.mode)
        else:
            nonce = b64decode(encoded_nonce)
            self.cipher = AES.new(self.key, self.mode, nonce = nonce)

    def encrypt(self, data):         
        return self.cipher.encrypt(data)
        
    def decrypt(self, data):
        return self.cipher.decrypt(data)

    def get_nonce(self):
        return b64encode(self.cipher.nonce).decode('utf-8')

    def get_key(self):
        return b64encode(self.key).decode('utf-8')
