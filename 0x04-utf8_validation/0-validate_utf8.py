#!/usr/bin/python3
""" A method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Count the remaining bytes to read
    for the current character
    """
    remaining_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if remaining_bytes > 0:
            # Check if the two most significant bits are '10'
            if (byte >> 6) == 0b10:
                remaining_bytes -= 1
            else:
                return False
        else:
            """Count the number of leading '1' bits
            to determine the character length
            """
            mask = 0b10000000
            while byte & mask:
                remaining_bytes += 1
                mask = mask >> 1

            # A single byte character
            if remaining_bytes == 0:
                continue

            # Invalid UTF-8 character length
            if remaining_bytes < 1 or remaining_bytes > 3:
                return False

    return remaining_bytes == 0
