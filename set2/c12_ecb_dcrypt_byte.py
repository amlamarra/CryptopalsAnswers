#!/usr/bin/env python3
import os
import sys
import base64
import random
import c09_pkcs7_padding
from c11_detection_oracle import detection_oracle
sys.path.append(os.path.abspath("../set1"))
from c07_aes_128_ecb import *  # Imports ecb_encrypt & ecb_decrypt

def ecb_encryption_oracle(instr, key):
    """ Encrypts in ECB mode under a random key with random padding
    both before and after the plaintext.
    ACCEPTS: One string & one byte string
    RETURNS: Base64 encoded string
    """
    
    hidden = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkga" \
           + "GFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdX" \
           + "N0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    
    msg = instr.encode() + base64.b64decode(hidden)
    msg = c09_pkcs7_padding.pad(msg, 16)
    
    return ecb_encrypt(msg, key)


def detect_block_size():
    """ Finds the block size the encryption oracle is using
    ACCEPTS: Nothing
    RETURNS: The block size as an integer
    """
    
    prev = ""
    encrypted = ecb_encryption_oracle("A", "YELLOW SUBMARINE".encode())
    i = 1
    while prev[:5] != encrypted[:5]:
        prev = encrypted
        i += 1
        encrypted = ecb_encryption_oracle("A"*i, "YELLOW SUBMARINE".encode())
        print(encrypted + "\n")
    
    return i - 1

def break_ecb():
    """ Attempt to decrypt the unknown string, one byte at a time
    ACCEPTS: 
    RETURNS: 
    """
    
    block_size = detect_block_size()
    
    print("The block size is {}".format(block_size))


if __name__ == "__main__":
    if os.path.isfile("key"):
        with open("key", "rb") as f:
            key = f.read()
    else:
        with open("key", "wb") as f:
            key = os.urandom(16)
            f.write(key)

    #with open("msg.txt") as f:
    #    msg = f.read()
    #print(ecb_encryption_oracle(msg, key))
    break_ecb()