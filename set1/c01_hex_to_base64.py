#!/usr/bin/python3
import argparse


def hex_to_base64(instr):
    """ Convert hex string to base64
    ACCEPTS: Hex string (even number of characters)
    RETURNS: Base64 string
    """
    
    CODESET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    i = 0
    final = ""
    while i < len(instr)-5:
        temp = int(instr[i:i+6],16)
        working = ""
        for x in range(4):
            working = CODESET[temp & 63] + working
            temp = temp >> 6
        final += working
        i += 6
    
    if len(instr) % 3 != 0:
        last = instr[i:]
        if len(last) == 2:
            final += (CODESET[int(last,16) >> 2]
                      + CODESET[(int(last,16) << 4) & 63]
                      + "==")
        elif len(last) == 4:
            final += (CODESET[int(last,16) >> 10]
                      + CODESET[(int(last,16) >> 4) & 63]
                      + CODESET[(int(last,16) << 2) & 63] 
                      + "=")
    return final


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Convert hex to base64")
    parser.add_argument("hex", nargs="?", help="The hex string")
    args = parser.parse_args()
    
    solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBs" \
               "aWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    if args.hex:
        hexstr = args.hex
    else:
        hexstr = "49276d206b696c6c696e6720796f757220627261696e206c" \
                 "696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_base64(hexstr))
