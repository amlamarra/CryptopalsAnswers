#!/usr/bin/python3
from c03_dcrypt_xor import *    # str_xor_c, dcrypt_xor, freq_score
from conversions import *

# This will use the list of hex strings in 04.txt and find the one that has
# been XOR'ed with a single byte.
strings = [line.strip() for line in open("04.txt")]
decrypted = [dcrypt_xor(hex_to_byte(string)) for string in strings]
scores = [freq_score(i[1]) for i in decrypted]
print(decrypted[scores.index(max(scores))][1])
