#!/usr/bin/python3
from str_to_hex import *

# Calculates the hamming distance of two strings
def ham_dist(str1, str2):
	xord = int(str_to_hex(str1),16) ^ int(str_to_hex(str2),16)
	
	count = 0
	while xord > 0:
		if xord % 2:
			count += 1
		xord >>= 1
	
	return count

if __name__ == "__main__":
	print(ham_dist("this is a test", "wokka wokka!!!"))
