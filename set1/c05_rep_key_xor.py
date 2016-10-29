#!/usr/bin/python3
import base64
from conversions import *
from c03_dcrypt_xor import dcrypt_xor
from c05_rep_key_xor import str_xor_key


def ham_dist(str1, str2):
    """ Calculates the hamming distance of two byte strings
    The Hamming distance is just the number of differing bits
    ACCEPTS: Two byte variables of equal length
    RETURNS: An integer of the Edit/Hamming Distance
    """
    
    count = 0
    for i in range(len(str1)):
        xord = str1[i] ^ str2[i]
        while xord > 0:
            if xord % 2:
                count += 1
            xord >>= 1
    
    return count


def normalized(inbytes, ksize):
    """ Calculates the normalized edit (hamming) distance between the
    first key size worth of bytes and the second key size worth of bytes
    ACCEPTS: A string of bytes and an integer representing the key size
    RETURNS: An integer of the normalized edit distance
    """
    
    if len(inbytes) < ksize * 4:
        raise NameError("Input bytes were not enough")
    
    block1 = ham_dist(inbytes[:ksize], inbytes[ksize:ksize*2])
    block2 = ham_dist(inbytes[:ksize], inbytes[ksize*2:ksize*3])
    block3 = ham_dist(inbytes[:ksize], inbytes[ksize*3:ksize*4])
    block4 = ham_dist(inbytes[ksize:ksize*2], inbytes[ksize*2:ksize*3])
    block5 = ham_dist(inbytes[ksize:ksize*2], inbytes[ksize*3:ksize*4])
    block6 = ham_dist(inbytes[ksize*2:ksize*3], inbytes[ksize*3:ksize*4])
    
    return ((block1 + block2 + block3 + block4 + block5 + block6) / 6) / ksize


def dcrypt_rep_key_xor(inbytes):
    """ Finds the key from a message XOR'ed with a repeating key
    ACCEPTS: A string of bytes
    RETURNS: The key as a string
    """
    
    sizes = [i for i in range(2, 41)]
    scores = [normalized(decoded, k) for k in sizes]
    index = scores.index(min(scores))
    ksize = sizes[index]
    
    tblocks = [b""] * ksize
    blocks = [decoded[i:i+ksize] for i in range(0, len(decoded), ksize)]
    for a in range(ksize):
        for block in blocks:
            if len(block) <= a:
                break
            tblocks[a] += chr(block[a]).encode()
    
    key = ""
    for tblock in tblocks:
        key += chr(dcrypt_xor(tblock)[0])
    
    return key


if __name__ == "__main__":
    
    with open("06.txt") as f:
        encoded = f.read()
    decoded = base64.b64decode(encoded)
    
    key = dcrypt_rep_key_xor(decoded)
    print("Extracted key:  {}".format(key))
    print(hex_to_str(str_xor_key(decoded, key)))
    
