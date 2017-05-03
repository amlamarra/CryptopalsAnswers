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

def encrypt_oracle_hidden(instr, key):
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


def find_block_size(key):
    """ Finds the block size the encryption oracle is using
    ACCEPTS: Nothing
    RETURNS: The block size as an integer
    """
    
    prev = ""
    encrypted = encrypt_oracle_hidden("A", key)
    i = 1
    # Just checking the first 4 characters
    while prev[:4] != encrypted[:4]:
        prev = encrypted
        i += 1
        encrypted = encrypt_oracle_hidden("A"*i, key)
        #print(encrypted + "\n")
    
    return i - 1


def break_ecb(key):
    """ Attempt to decrypt the unknown string, one byte at a time
    ACCEPTS: 
    RETURNS: 
    """
    
    # Find the block size
    block_size = find_block_size(key)
    print("The block size is {}".format(block_size))
    
    # Generate encrypted text with the same letter twice that of block_size
    # If ECB mode is being used, then the 2 blocks should be identical
    encrypted = encrypt_oracle_hidden("A" * (block_size*2), key)
    print("Mode: {}".format(detection_oracle(encrypted)))
    
    # Save the first block with all A's & the first character of 'hidden'
    block1 = base64.b64decode(encrypt_oracle_hidden(
        "A" * (block_size-1), key))[:block_size]
    
    # Create a dictionary of first blocks with every possible last byte
    dictionary = [base64.b64decode(encrypt_oracle_hidden("A" * (block_size-1)
                  + chr(i), key))[:block_size] for i in range(128)]
    
    if block1 in dictionary:
        index = dictionary.index(block1)
        print("The first character is: {}".format(chr(index)))
    else:
        print("We ain't found shit...\nDictionary dump:")
        for item in dictionary:
            print(item)


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
    #print(encrypt_oracle_hidden(msg, key))
    break_ecb(key)