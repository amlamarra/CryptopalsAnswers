#!/usr/bin/python3

# XOR two hex strings
def str_xor(str1, str2):
	# ACCEPTS: Two hex strings of equal length
	# RETURNS: One hex string
	string = str(hex(int(str1,16) ^ int(str2,16)))[2:]
	
	# If the first hex character starts with 0, it would be left off
	# This will ensure it's put back on
	if len(string) % 2:
		string = "0" + string
	return string

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
