#!/usr/bin/python3

# Takes a string of ASCII characters and returns a string of hex characters
def str_to_hex(instr):
	return "".join([str(hex(ord(i))).lstrip("0x") for i in instr])

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(
		description="Converts an ASCII string to a string of hex characters")
	parser.add_argument("string", nargs="?", help="The ASCII string")
	args = parser.parse_args()
	if args.string:
		instr = args.string
	else:
		instr = input("Enter the string: ")
	
	print(str_to_hex(instr))
