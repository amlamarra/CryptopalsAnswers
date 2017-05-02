#!/usr/bin/env python3
""" Implement AES 128 CBC
Initialization Vector will be 16 null bytes (\x00\x00\x00 ...)
Key = "YELLOW SUBMARINE"
Command line encrypting:
$ openssl enc -aes-128-cbc -base64 -in in.txt
  -K "59454c4c4f57205355424d4152494e45" -iv "00000000000000000000000000000000"
Command line decrypting:
$ openssl enc -aes-128-cbc -d -base64 -in out.txt
  -K "59454c4c4f57205355424d4152494e45" -iv "00000000000000000000000000000000"
"""

import base64
import sys
import os
import c09_pkcs7_padding
sys.path.append(os.path.abspath("../set1"))
from c07_aes_128_ecb import * # Imports ecb_encrypt & ecb_decrypt
from c02_str_xor import str_xor
from conversions import * # str_to_hex, hex_to_str, byte_to_hex, hex_to_byte


def cbc_encrypt(plain_text, key, initialization_vector):
    """ Encrypts a plaintext message using AES 128 CBC mode
    ACCEPTS: Three byte strings (plain text, key & IV)
    RETURNS: Base64 encoded string
    """
    
    if len(key) != 16 or len(initialization_vector) != 16:
        raise NameError("Key or initialization vector not 16 bytes long")
    
    padded_text = c09_pkcs7_padding.pad(plain_text, 16)
    
    blocks = [padded_text[i:i+16] for i in range(0, len(padded_text), 16)]
    content = b""
    prev = initialization_vector
    for block in blocks:
        xord = str_xor(byte_to_hex(block), byte_to_hex(prev))
        prev = base64.b64decode(ecb_encrypt(hex_to_byte(xord), key))
        content += prev
    
    content = base64.b64encode(content).decode()
    
    # Adding a new line every 64 characters to match the openssl command
    final = ""
    for i in range(0, len(content), 64):
        final += content[i:i+64] + "\n"
    final = final[:-1]
    
    return final


def cbc_decrypt(cipher_text, key, initialization_vector):
    """ Encrypts a plaintext message using AES 128 CBC mode
    ACCEPTS: Two strings (base64 ciphertext & key) & one byte string (IV)
    RETURNS: A string (the plaintext message)
    """
    
    if len(key) != 16 or len(initialization_vector) != 16:
        raise NameError("Key or initialization vector not 16 bytes long")
    
    content = base64.b64decode(cipher_text)
    blocks = [content[i:i+16] for i in range(0, len(content), 16)]
    
    plain_text = b""
    prev = initialization_vector
    for block in blocks:
        temp = ecb_decrypt(base64.b64encode(block), key)
        xord = str_xor(byte_to_hex(temp), byte_to_hex(prev))
        plain_text += hex_to_byte(xord)
        prev = block
    
    # Is there padding? If so, remove it.
    plen = plain_text[-1]   # Padding length
    if plain_text[-plen:] == (len(plain_text[-plen:]) * chr(plen)).encode():
        plain_text = plain_text[:-plen]
    
    return plain_text.decode()


if __name__ == "__main__":
    
    key = "YELLOW SUBMARINE"
    iv = b"\x00" * 16
    
    with open("10.txt") as f:
        content = f.read()
    decrypted = cbc_decrypt(content, key, iv)
    print(decrypted)
    
