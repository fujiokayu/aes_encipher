# aes_encipher

Encrypt / Decrypt your file by using AES CTR Mode.

## usage

### Prerequisites

Need some packages, written in Pipfile.  
Ofcourse you need python, too.

And, you have to know the fact that I'm not tested enough.

### encrypt mode

```
python aes_encipher.py e file_to_encrypt
```

When you encrypt your file, the key and nonce will make automaticaly, 
and will encode them to base64.
Its need to decrypt the file.

### decrypt mode

```
python aes_encipher.py d file_to_decrypt --nonce base64encoded_nonce --key base64encoded_key
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

* * *

This product is provited AS IS and with all faults without warranty or conditions of any kind.
