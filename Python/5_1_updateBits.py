# updateBits.py
#########################################################################################
# Author  : Hong
# Created : 23/11/2017
# Modified: 23/11/2017
# Notes   : [5.1] You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
#                method to insert M into N such that M starts at bit j and ends at bit i. You can assume
#                that the bits j through i have enough space to fit all ofM. That is, if M= 10011,
#                you can assume that there are at least 5 bits between j and i. You would not, for
#                example, have j-3 and i=2, because M could not fully fit between bit 3 and bit 2.
#                EXAMPLE:
#                Input: N = 10000000000, M = 10011, i = 2, j = 6
#                Output: N = 10001001100
#########################################################################################
import unittest, os


def updateBits(n, m, i, j):
    # Create a mask to clear bits i through j in n
    # EXAMPLE: i = 2, j = 4. Result should be 11100011.
    # For simplicity, we'll use just 8 bits for the example
    allOnes = ~0  # will equal sequence of all 1s

    # 1s before position j, then 0s. left = 11100000
    left = allOnes << (j + 1)

    # 1s after position i. right = 00000011
    right = ((1 << i) - 1)

    # All 1s, except for 0s between i and j. mask = 11100011
    mask = left | right

    # Clear bits j through i then put m in there
    n_cleared = n & mask  # Clear bits j through i
    m_shifted = m << i  # Move m into correct position

    return n_cleared | m_shifted  # OR them, and we're done!


class updateBits_test(unittest.TestCase):
    def test(self):
        A = 1024  # 100 0000 0000
        B = 19  # 1 0011
        print("binary number:", bin(updateBits(A, B, 2, 6)))
        print("decimal number:", updateBits(A, B, 2, 6))

        C = 0b10000000000
        D = 0b10011
        print("binary number:", bin(updateBits(C, D, 2, 6)))
        print("decimal number:", (updateBits(C, D, 2, 6)))

        os.system("Pause")


unittest.main()
