#!/usr/bin/python3
""" A method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Count the number of leading 1s in the byte"""
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    # Check if the byte is a valid start of a multi-byte sequence
    def isValidStart(byte):
        leadingOnes = countLeadingOnes(byte)
        if leadingOnes == 1 or leadingOnes > 4:
            return False
        return True

    # Main validation logic
    i = 0
    while i < len(data):
        leadingOnes = countLeadingOnes(data[i])
        if not isValidStart(data[i]):
            return False
        if leadingOnes > 1:
            i += 1
            for j in range(i, i + leadingOnes - 1):
                if j >= len(data) or countLeadingOnes(data[j]) != 1:
                    return False
                i += 1
        i += 1

    return True
