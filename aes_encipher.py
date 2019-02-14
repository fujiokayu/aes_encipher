import argparse
import struct
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

MAX_BUFFER_SIZE = 4096
KEY_LENGTH = 32

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    parser.add_argument('arg1', help='chose e (encrypt) or d (decrypt)')
    parser.add_argument('arg2', help='file to en/de-crypt')
    args = parser.parse_args()

    with open(args.arg2, 'rb') as f:
        for bytes in iter(lambda: f.read(MAX_BUFFER_SIZE), b''):
            data = bytes

    key = get_random_bytes(KEY_LENGTH)
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(data)

    result = json.dumps({
        'nonce':b64encode(cipher.nonce).decode('utf-8'), 
        'ciphertext':b64encode(ct_bytes).decode('utf-8'), 
        'base64 key':b64encode(key).decode('utf-8')})
    print(result)
