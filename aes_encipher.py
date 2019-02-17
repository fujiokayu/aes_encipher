import sys
import os
import argparse
import struct
import json
from base64 import b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from AesEncipher import AesEncipher


MAX_BUFFER_SIZE = 4096
KEY_LENGTH = 32


def set_argument_parser():

    parser = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    parser.add_argument('tool_mode', help='chose e (encrypt) or d (decrypt)')
    parser.add_argument('input_file', help='file to en/de-crypt')
    parser.add_argument('--nonce', help='nonce to decrypt', type = str, default = "")
    parser.add_argument('--key', help='key to decrypt', type = str, default = "")
    return parser.parse_args()


def check_args(args):

    if args.tool_mode != 'e' and args.tool_mode != 'd':
        print("error: args1: undefined parameter")
        sys.exit()
    if not os.path.isfile(args.input_file):
        print("error: args2: file not exists")
        sys.exit()
    if args.tool_mode == 'd' and args.nonce == "":
        print("error: --nonce is null: need nonce to use decrypt mode")
        sys.exit()
    if args.tool_mode == 'd' and args.key == "":
        print("error: --key is null: need key to use decrypt mode")
        sys.exit()


if __name__ == '__main__':
    
    args = set_argument_parser()
    check_args(args)

    encrypt_mode = True if args.tool_mode == 'e' else False

    key = get_random_bytes(KEY_LENGTH) if args.key == "" else b64decode(args.key)
    aes_encipher = AesEncipher(AES.MODE_CTR, key)
    translated_bytes = bytearray(b"")

    with open(args.input_file, 'rb') as f:
        for bytes in iter(lambda: f.read(MAX_BUFFER_SIZE), b''):
            if encrypt_mode:
                translated_bytes.extend(aes_encipher.encrypt(bytes))
                encrypt_info = json.dumps({'nonce':aes_encipher.get_nonce(), 'key':aes_encipher.get_key()})
                print(encrypt_info)
            else :
                translated_bytes.extend(aes_encipher.decrypt(bytes, b64decode(args.nonce)))

    out_file_name = args.input_file
    out_file_name += "_encrypted" if encrypt_mode else "_decrypted"
    with open(out_file_name,'wb') as translated_file :
        translated_file.write(translated_bytes)
