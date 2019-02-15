import argparse
import struct
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

MAX_BUFFER_SIZE = 4096
KEY_LENGTH = 32


class AesEncypher:
    def __init__(self, mode, key):
        self.key = key
        self.mode = mode

    def encrypt(self, data):
        cipher = AES.new(self.key, self.mode)
        ct_bytes = cipher.encrypt(data)
        return b64encode(ct_bytes).decode('utf-8')
        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    parser.add_argument('arg1', help='chose e (encrypt) or d (decrypt)')
    parser.add_argument('arg2', help='file to en/de-crypt')
    args = parser.parse_args()

    key = get_random_bytes(KEY_LENGTH)
    aes_encipher = AesEncypher(AES.MODE_CTR, key)
    cipher_text = ""
    with open(args.arg2, 'rb') as f:
        for bytes in iter(lambda: f.read(MAX_BUFFER_SIZE), b''):
            cipher_text += aes_encipher.encrypt(bytes)

    print(cipher_text)

