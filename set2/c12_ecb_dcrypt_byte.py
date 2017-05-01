#!/usr/bin/python3
import random
import os
import sys
sys.path.append(os.path.abspath("../set1"))
from c07_aes_128_ecb import * # Imports ecb_encrypt & ecb_decrypt
import c09_pkcs7_padding
        
def encryption_oracle(instr):
    """ Encrypts randomly, between ECB & CBC, under a random key with random
    padding both before and after the plaintext.
    ACCEPTS: One string
    RETURNS: Base64 encoded string
    """
    
    hidden = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
           + "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
           + "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
           + "YnkK"
    
    msg = bytes(instr.encode()) + base64.b64decode(hidden)
    msg = c09_pkcs7_padding.pad(msg, 16)
    
    key = os.urandom(16)
    
    print("Encrypting in ECB\n")
    encrypted = ecb_encrypt(msg, key)
    
    return encrypted


if __name__ == "__main__":
    if os.path.isfile("key"):
        with open("key", "rb") as f:
            key = f.read()
    else:
        with open("key", "wb") as f:
            key = os.urandom(16)
            f.write(key)
