#!/usr/bin/python3
import os
import sys
from random import randrange
sys.path.append(os.path.abspath("../set1"))
from c07_aes_128_ecb import * # Imports ecb_encrypt & ecb_decrypt
import c09_pkcs7_padding
from c10_aes_128_cbc import * # Imports cbc_encrypt & cbc_decrypt


def gen_rand(length):
    """ Returns a random byte string of the specified length
    ACCEPTS: Integer
    RETURNS: Byte string
    """
    
    return os.urandom(length)


def encryption_oracle(instr):
    """ Encrypts randomly, between ECB & CBC, under a random key with random
    padding both before and after the plaintext.
    ACCEPTS: One string
    RETURNS: Base64 encoded string
    """
    
    pretext = gen_rand(randrange(5, 11))
    posttext = gen_rand(randrange(5, 11))
    msg = pretext + bytes(instr.encode()) + posttext
    msg = c09_pkcs7_padding.pad(msg, 16)
    
    mode = randrange(2)
    key = gen_rand(16)
    if mode:
        IV = gen_rand(16)
        encrypted = cbc_encrypt(msg, key, IV)
    else:
        encrypted = ecb_encrypt(msg, key)
        
    return encrypted


if __name__=="__main__":
    text = "This is a plain text message."
    encrypted = encryption_oracle(text)
    print("Length of encrypted message: {}".format(len(encrypted)))
    print(encrypted)
