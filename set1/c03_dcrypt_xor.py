#!/usr/bin/python3
from hex_to_str import hex_to_str
import argparse

# XOR a string with a single character
def str_xor_c(instr, char):
	# RECEIVES: Ascii string & ascii character
	# RETURNS: Ascii string XOR'ed with the character
	return "".join([chr(ord(instr[c])^ord(char)) for c in range(len(instr))])

# Find the key a string was XOR'ed with
def find_xor_key(xorstr):
	# RECEIVES: String of XOR'ed characters in hex
	# RETURNS: Decimal value of the character the string was XOR'ed with
	
	freqs = { # www.data-compression.com/english.html
		'a': 651738,
		'b': 124248,
		'c': 217339,
		'd': 349835,
		'e': 1041442,
		'f': 197881,
		'g': 158610,
		'h': 492888,
		'i': 558094,
		'j': 9033,
		'k': 50529,
		'l': 331490,
		'm': 202124,
		'n': 564513,
		'o': 596302,
		'p': 137645,
		'q': 8606,
		'r': 497563,
		's': 515760,
		't': 729357,
		'u': 225134,
		'v': 82903,
		'w': 171272,
		'x': 13692,
		'y': 145984,
		'z': 7836,
		' ': 1918182
	}
	string = hex_to_str(xorstr)
	
	highscore = 0
	for i in range(256):
		score = 0
		decrypted = str_xor_c(string, chr(i))
		for c in decrypted:
			if c.lower() in freqs:
				score += freqs[c.lower()]
		if score > highscore:
			highscore = score
			key = i
	
	return key

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
			 "Find the character a string was XOR'ed with")
	parser.add_argument("hex", nargs="?", help="The XOR'ed hex string")
	args = parser.parse_args()
	
	if args.hex:
		code = args.hex
	else:
		code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	key = find_xor_key(code)
	print("Key = {}".format(key))
	print("String = {}".format(str_xor_c(hex_to_str(code), chr(key))))
