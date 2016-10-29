#!/usr/bin/python3
from conversions import *
import argparse
from Crypto.Util.strxor import strxor_c


def str_xor_c(instr, char):
    """ XOR a string with a single character
    ACCEPTS: Ascii string & ascii character
    RETURNS: Ascii string XOR'ed with the character
    """
    
    return "".join([chr(instr[c] ^ ord(char)) for c in range(len(instr))])


def freq_score(instr):
    """ A score is added up based on the frequency of each letter in English
    ACCEPTS: Ascii string
    RETURNS: Integer of the frequency score
    """
    
    freqs = { # www.data-compression.com/english.html
        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182
    }
    
    score = 0
    for c in instr.lower():
            if c in freqs:
                score += freqs[c]
    return score


def dcrypt_xor(bytes):
    """ Find the key a string was XOR'ed with
    ACCEPTS: String of byte characters
    RETURNS: A tuple of the key and the decrypted string
    The key is the decimal value of the character the string was XOR'ed with
    """
    
    scores = [freq_score(str_xor_c(bytes, chr(i))) for i in range(256)]
    key = scores.index(max(scores))
    
    return (key, str_xor_c(bytes, chr(key)))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=
             "Find the character a string was XOR'ed with")
    parser.add_argument("hex", nargs="?", help="The XOR'ed hex string")
    args = parser.parse_args()
    
    if args.hex:
        code = args.hex
    else:
        code = "1b37373331363f78151b7f2b783431333d" \
               "78397828372d363c78373e783a393b3736"
    answer = dcrypt_xor(hex_to_byte(code))
    print("Key = {}".format(answer[0]))
    print("String = {}".format(answer[1]))
