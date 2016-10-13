#!/usr/bin/python3

# Takes a string (even number) of hex characters and returns a string
def hex_to_str(in_str):
	return "".join([chr(int(in_str[i*2:i*2+2],16)) 
			for i in range(int(len(in_str)/2))])

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(
		description="Converts hex characters to an ascii string")
	parser.add_argument("hex", nargs="?", help="The hex string")
	args = parser.parse_args()
	if args.hex:
		instr = args.hex
	else:
		instr = input("Enter the hex: ")
	
	print(hex_to_str(instr))
