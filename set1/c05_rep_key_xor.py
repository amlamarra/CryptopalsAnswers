#!/usr/bin/python3
import argparse
from c02_str_xor import *
from conversions import *


def str_xor_key(msg, key):
    """ XOR a string with a repeating key
    ACCEPTS: Either a string or bytes for both the message & key
    RETURNS: a hex string
    """
    
    if type(msg) is str:
        msg = str_to_hex(msg)
    elif type(msg) is bytes:
        msg = byte_to_hex(msg)
    
    if type(key) is str:
        key = str_to_hex(key)
    elif type(key) is bytes:
        key = byte_to_hex(key)
    
    mlen = len(msg)
    klen = len(key)
    
    # Make the string length evenly divisible by the key length
    if mlen % klen:
        msg += "0" * (klen - (mlen % klen))
    
    out_str = "".join([str_xor(msg[i:i+klen], key)
                      for i in range(0, len(msg), klen)])
    
    return out_str[:mlen]


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Repeating-key XOR with a " \
                                     "longer string (the key is shorter)")
    parser.add_argument("string", nargs="?", help="The string in ASCII")
    parser.add_argument("key", nargs="?", help="The key to XOR with the string")
    args = parser.parse_args()
    
    if args.string:
        STRING = args.string
    else:
        STRING = "Burning 'em, if you ain't quick and " \
                 "nimble I go crazy when I hear a cymbal"
    
    if args.key:
        KEY = args.key
    else:
        KEY = "ICE"
    
    print("Original message:")
    print(STRING)
    print("The key: {}".format(KEY))
    
    print("\nMessage encrypted with key:")
    print(str_xor_key(STRING, KEY))
