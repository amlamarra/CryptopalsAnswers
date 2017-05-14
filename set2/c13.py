#!/usr/bin/env python3
import re


def parser(instr):
    """ Parses URL parameters and converts to a dict object
    ACCEPTS: One string
    RETURNS: One dict
    """
    
    return {s.split("=")[0]:s.split("=")[1] for s in instr.split("&")}


def profile_for(email):
    """ Provides a profile for a supplied email address
    ACCEPTS: One string (email address)
    RETURNS: One dict
    """
    
    email = email.replace("&","").replace("=","")
    
    print("Safe: {}".format(email))


if __name__ == "__main__":
    
    obj = parser("foo=bar&baz=qux&zap=zazzle")
    print(obj)
    #profile_for("andrew@lamarra.com")
    while True:
        email = input("Validate email: ")
        profile_for(email)