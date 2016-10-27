#!/usr/bin/python3
import argparse


def str_xor(hex1, hex2):
    """ XOR two hex strings
    ACCEPTS: Two hex strings of equal length
    RETURNS: One hex string
    """
    
    if len(hex1) != len(hex2):
        raise NameError("The hex strings passed to str_xor need to equal in length")
    
    string = str(hex(int(hex1,16) ^ int(hex2,16)))[2:]
    
    # If the resulting hex string is supposed to be prefixed with zeros,
    # normally, they'd be left off. This will ensure it's put back on.
    if len(hex1) % len(string):
        string = "0"*(len(hex1) - len(string)) + string
    
    return string


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="XOR two strings of equal length")
    parser.add_argument("string1", nargs="?", help="The first string")
    parser.add_argument("string2", nargs="?", help="The second string")
    args = parser.parse_args()
    
    if args.string1:
        str1 = args.string1
    else:
        str1 = "1c0111001f010100061a024b53535009181c"
    
    if args.string2:
        str2 = args.string2
    else:
        str2 = "686974207468652062756c6c277320657965"
    print(str_xor(str1, str2))
