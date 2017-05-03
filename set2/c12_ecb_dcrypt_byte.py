#!/usr/bin/env python3
import os
import sys
import base64
import random
import c09_pkcs7_padding
from c11_detection_oracle import detection_oracle
sys.path.append(os.path.abspath("../set1"))
from c07_aes_128_ecb import ecb_encrypt


# KEY = "YELLOW SUBMARINE"

def encrypt_oracle_hidden(instr, secret = b""):
    """ Encrypts a message with a random key. If a secret message (byte
    string) is supplied, that is appended to the end of the message.
    ACCEPTS: One string, & optionally, one byte string
    RETURNS: Base64 encoded string
    """
    
    # Create a random key, but keep it consistent
    if os.path.isfile("key"):
        with open("key", "rb") as f:
            key = f.read()
    else:
        with open("key", "wb") as f:
            key = os.urandom(16)
            f.write(key)
    
    msg = instr.encode() + secret
    msg = c09_pkcs7_padding.pad(msg, 16)
    
    return ecb_encrypt(msg, key)


def find_block_size():
    """ Finds the block size the encryption oracle is using
    ACCEPTS: Nothing
    RETURNS: The block size as an integer
    """
    
    prev = ""
    encrypted = encrypt_oracle_hidden("A")
    i = 1
    # Checking the first 4 base64'ed characters should be enough
    while prev[:4] != encrypted[:4]:
        prev = encrypted
        i += 1
        encrypted = encrypt_oracle_hidden("A"*i)
    
    return i - 1


def break_ecb(secret):
    """ Attempt to decrypt the unknown string, one byte at a time
    ACCEPTS: Base64 encoded secret string
    RETURNS: One string containing the secret message
    """
    
    # Find the block size
    block_size = find_block_size()
    print("The block size is {}".format(block_size))
    
    # Generate encrypted text with the same letter twice that of block_size
    # If ECB mode is being used, then the 2 blocks should be identical
    encrypted = encrypt_oracle_hidden("A" * (block_size*2))
    print("Mode: {}".format(detection_oracle(encrypted)))
    
    # Create a dictionary of first blocks with every possible last byte
    dictionary = [base64.b64decode(encrypt_oracle_hidden("A" * (block_size-1)
                  + chr(i)))[:block_size] for i in range(128)]
    
    scrt_msg = base64.b64decode(secret)
    dcryptd_msg = ""
    for i in range(len(scrt_msg)):
        # Save the first block with all A's & one character of 'secret'
        block1 = base64.b64decode(encrypt_oracle_hidden(
            "A" * (block_size-1), scrt_msg[i:i+1]))[:block_size]
        
        try:
            index = dictionary.index(block1)
            #print("The first character is: {}".format(chr(index)))
            dcryptd_msg += chr(index)
        except ValueError:
            print("A byte was not found in the dictionary")
    
    return dcryptd_msg

if __name__ == "__main__":
    
    secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkga" \
           + "GFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdX" \
           + "N0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

    print("The secret message:\n{}".format(break_ecb(secret)))