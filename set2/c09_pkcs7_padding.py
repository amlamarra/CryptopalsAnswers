#!/usr/bin/python3
import argparse


def pad(text, bsize):
    """ Pads the given text so it's a multiple of the given block size.
    ACCEPTS: One string & One integer (< 256)
    RETURNS: A byte string
    """
    
    if bsize >= 256:
        raise NameError("The supplied block size is too high.")
    
    pad_size = 0
    if len(text) % bsize:
        pad_size = bsize - (len(text) % bsize)
    text += chr(pad_size) * pad_size
    
    return text.encode()


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Implement PKCS #7 padding on some text.")
    parser.add_argument("-s", "--string", help="The string that needs padding")
    parser.add_argument("-b", "--block_size", type=int, help="The size of each block")
    args = parser.parse_args()
    
    if args.string:
        text = args.string
    else:
        text = "YELLOW SUBMARINE"
    
    if args.block_size:
        bsize = args.block_size
    else:
        bsize = 20
    
    print(pad(text, bsize))
