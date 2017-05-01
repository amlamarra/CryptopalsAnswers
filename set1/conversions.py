#!/usr/bin/python3

def str_to_hex(in_str):
    """ Convert string to hex
    Converts a string of ASCII characters to a string of hex characters.
    """
    
    out_str = ""
    for i in in_str:
        out_str += str(hex(ord(i)))[2:]
        # hex() will remove any leading zeros, this will put them back.
        if len(out_str) % 2:
            out_str = out_str[:-1] + "0" + out_str[-1:]
    
    return out_str


def hex_to_str(hex_str):
    """ Convert hex to ASCII string
    Converts a string of hex characters to a string of ASCII characters.
    """
    
    return "".join([chr(int(hex_str[i*2:i*2+2],16))
                    for i in range(int(len(hex_str)/2))])


def byte_to_hex(byte_str):
    """ Convert bytes to hex
    Converts a byte string to it's hex string representation.
    """
    
    out_str = ""
    for i in byte_str:
        out_str += str(hex(i))[2:]
        # hex() will remove any leading zeros, this will put them back.
        if len(out_str) % 2:
            out_str = out_str[:-1] + "0" + out_str[-1:]
        
    return out_str


def hex_to_byte(hex_str):
    """ Convert hex to bytes
    Converts a string of hex characters to a string of byte characters.
    """
    
    #byte_str = ""
    #for i in range(0, len(hex_str), 2):
    #    byte_str += chr(int(hex_str[i:i+2], 16))
    #return byte_str.encode()
    
    return bytes(bytearray.fromhex(hex_str))
