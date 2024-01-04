#!/usr/bin/python3
""" A method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_remaining = 0

    for i in data:
        if byte_remaining == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_remaining = 1
            elif i >> 4 == 0b1110:
                byte_remaining = 2
            elif i >> 3 == 0b11110:
                byte_remaining = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_remaining -= 1
    return byte_remaining == 0
