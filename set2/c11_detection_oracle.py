#!/usr/bin/env python3.5
import os
import sys
import base64
from random import randrange, randint
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
    
    pretext = gen_rand(randint(5, 10))
    posttext = gen_rand(randint(5, 10))
    
    msg = pretext + bytes(instr.encode()) + posttext
    msg = c09_pkcs7_padding.pad(msg, 16)
    
    key = gen_rand(16)
    if randrange(2):
        IV = gen_rand(16)
        print("Encrypting in CBC\n")
        encrypted = cbc_encrypt(msg, key, IV)
    else:
        print("Encrypting in ECB\n")
        encrypted = ecb_encrypt(msg, key)
    
    return encrypted


def detection_oracle(encrypted):
    """ Detects which encryption mode (ECB or CBC) is happening
    ACCEPTS: A string of base64 characters
    RETURNS: The string "ECB" or "CBC"
    """
    encrypted_msg = base64.b64decode(encrypted)
    
    for init in range(16):
        blocks = [encrypted_msg[i+init:i+init+16] for i in range(0, len(encrypted_msg), 16)]
        
        seen = set()
        for block in blocks:
            if block in seen:
                print("Duplicate block: {}".format(block))
                return "ECB"
            else:
                seen.add(block)
            
    return "CBC"


if __name__=="__main__":
    text = "A" * 48
    encrypted = encryption_oracle(text)
    
    print("Detected {} mode".format(detection_oracle(encrypted)))
