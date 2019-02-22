# tiny_encryptor

Encrypt / Decrypt your file by using AES CTR Mode.

## usage

### Prerequisites

```
pip install pycryptodome
```  
or  
```
pipenv install
```

### encrypt mode

```
python tiny_encryptor.py e file_to_encrypt
```

When you encrypt your file, the key and nonce will make automaticaly, and will encode them to base64.  
Its need to decrypt the file.  

If you want to use specific key and nonce, set args as below; 
```
python tiny_encryptor.py e file_to_encrypt --nonce base64encoded_nonce --key base64encoded_key
```

### decrypt mode

```
python tiny_encryptor.py d file_to_decrypt --nonce base64encoded_nonce --key base64encoded_key
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

* * *

This product is provited AS IS and with all faults without warranty or conditions of any kind.
