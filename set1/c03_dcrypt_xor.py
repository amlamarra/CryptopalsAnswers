#!/usr/bin/python3
from hex_to_str import hex_to_str
import argparse

# XOR a string with a single character
def str_xor_c(instr, char):
	# ACCEPTS: Ascii string & ascii character
	# RETURNS: Ascii string XOR'ed with the character
	return "".join([chr(ord(instr[c])^ord(char)) for c in range(len(instr))])

def freq_score(instr):
	# ACCEPTS: Ascii string
	# RETURNS: Integer of the frequency score
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
	score = 0
	for c in instr:
			if c.lower() in freqs:
				score += freqs[c.lower()]
	return score

# Find the key a string was XOR'ed with
def dcrypt_xor(xorstr):
	# ACCEPTS: String of XOR'ed characters in hex
	# RETURNS: A tuple of the key and the decrypted string
		# The key is the decimal value of the character the string was XOR'ed with
	string = hex_to_str(xorstr)
	scores = [freq_score(str_xor_c(string, chr(i))) for i in range(256)]
	key = scores.index(max(scores))
	return (key, str_xor_c(string, chr(key)))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
			 "Find the character a string was XOR'ed with")
	parser.add_argument("hex", nargs="?", help="The XOR'ed hex string")
	args = parser.parse_args()
	
	if args.hex:
		code = args.hex
	else:
		code = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	answer = dcrypt_xor(code)
	print("Key = {}".format(answer[0]))
	print("String = {}".format(answer[1].encode('utf-8')))
