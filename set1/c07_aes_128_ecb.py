#!/usr/bin/python3
# Decrypting on the command line:
# openssl enc -aes-128-ecb -d -base64 -in 07.txt -K "59454c4c4f57205355424d4152494e45"
# The key: YELLOW SUBMARINE

from Crypto.Cipher import AES
import base64

def encrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_ECB)
    return base64.b64encode(aes.encrypt(message))

def decrypt(encrypted, passphrase):
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))

if __name__ == "__main__":
    with open("07.txt") as f:
        encrypted = f.read()

    passphrase = "YELLOW SUBMARINE"
    print(decrypt(encrypted, passphrase).decode())
