#!/usr/bin/python3
from c02_str_xor import *
from str_to_hex import *
import argparse

def str_xor_key(instr, key):
	strlen = len(instr)
	keylen = len(key)
	
	# Make the string length evenly divisible by the key length
	if strlen % keylen:
		instr += "a" * (keylen - (strlen % keylen))
	
	outstr = "".join([str_xor(str_to_hex(instr[i*keylen:i*keylen+keylen]), str_to_hex(key)) 
					  for i in range(int(len(instr)/keylen))])
	
	# Here's the same thing, but more readable
	#outstr = ""
	#for i in range(int(len(instr)/keylen)):
	#	outstr += str_xor(str_to_hex(instr[i*keylen:i*keylen+keylen]), str_to_hex(key))
	
	return outstr[:strlen*2]
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Repeating-key XOR with a longer string \
									 (make sure the key is shorter)")
	parser.add_argument("string", nargs="?", help="The string in ASCII")
	parser.add_argument("key", nargs="?", help="The key to XOR with the string")
	args = parser.parse_args()
	
	if args.string:
		STRING = args.string
	else:
		STRING = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
	
	if args.key:
		KEY = args.key
	else:
		KEY = "ICE"
	
	print(str_xor_key(STRING, KEY))
