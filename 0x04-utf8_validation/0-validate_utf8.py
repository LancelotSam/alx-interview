#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):

    def is_valid(byte, mask, compare):
        return (byte & mask) == compare

    n_bytes = 0

    for byte in data:
        if n_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if is_valid(byte, 0b10000000,
                        0b00000000):  # 1-byte character (0xxxxxxx)
                n_bytes = 0
            elif is_valid(byte, 0b11100000,
                          0b11000000):  # 2-byte character (110xxxxx)
                n_bytes = 1
            elif is_valid(byte, 0b11110000,
                          0b11100000):  # 3-byte character (1110xxxx)
                n_bytes = 2
            elif is_valid(byte, 0b11111000,
                          0b11110000):  # 4-byte character (11110xxx)
                n_bytes = 3
            else:
                return False
        else:
            # Check that continuation bytes start with 10xxxxxx
            if not is_valid(byte, 0b11000000, 0b10000000):
                return False
            n_bytes -= 1

    return n_bytes == 0
