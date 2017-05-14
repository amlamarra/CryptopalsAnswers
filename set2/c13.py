#!/usr/bin/env python3


def parser(instr):
    """ Parses URL parameters and converts to a dict object
    ACCEPTS: One string
    RETURNS: One dict
    """

    return {s.split("=")[0]: s.split("=")[1] for s in instr.split("&")}


def encode_profile(profile):
    """ Encodes a given profile in URL format
    ACCEPTS: One dict (the profile)
    RETURNS: One string (the URL format)
    """

    ret = ""



def profile_for(email):
    """ Provides a profile for a supplied email address
    ACCEPTS: One string (email address)
    RETURNS: One dict
    """

    email = email.replace("&", "").replace("=", "")

    print("Safe: {}".format(email))
    profile = parser("email={}&uid=10&role=user".format(email))
    encode_profile(profile)


if __name__ == "__main__":

    obj = parser("foo=bar&baz=qux&zap=zazzle")
    print(obj)
