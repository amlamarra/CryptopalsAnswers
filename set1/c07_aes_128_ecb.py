#!/usr/bin/python3
""" Decrypting on the command line:
$ openssl enc -aes-128-ecb -d -base64 -in 07.txt -K "59454c4c4f57205355424d4152494e45"
The key: YELLOW SUBMARINE
"""

from Crypto.Cipher import AES
import base64


def ecb_encrypt(message, passphrase):
    """ Encrypts a message in AES ECB mode with a given key
    ACCEPTS: Two byte strings, the plaintext message and the key
    RETURNS: A string of base64 encoded ciphertext
    """
    
    aes = AES.new(passphrase, AES.MODE_ECB)
    content = base64.b64encode(aes.encrypt(message)).decode()
    
    # Adding a new line every 64 characters to match the openssl command
    final = ""
    for i in range(0, len(content), 64):
        final += content[i:i+64] + "\n"
    final = final[:-1]
    
    return final


def ecb_decrypt(encrypted, passphrase):
    """ Decrypts a ciphertext in AES ECB mode with a given key
    ACCEPTS: Two strings, the base64 encoded ciphertext and the key
    RETURNS: A bytes string of the plaintext message
    """
    
    aes = AES.new(passphrase, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))


if __name__ == "__main__":
    with open("07.txt") as f:
        encrypted = f.read()

    passphrase = "YELLOW SUBMARINE"
    print(ecb_decrypt(encrypted, passphrase).decode())