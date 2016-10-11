#!/usr/bin/python3

# Takes 2 strings of equal length, XORs them, and returns them
def str_xor(str1, str2):
    return str(hex(int(str1,16) ^ int(str2,16)))[2:]

if __name__ == "__main__":
	import argparse
	
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
