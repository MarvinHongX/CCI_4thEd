# bitSwapRequire.py
#########################################################################################
# Author  : Hong
# Created : 23/11/2017
# Modified: 24/11/2017
# Notes   : [5.5] Write a function to determine the number of bits required to convert integer A to
#                integer B.
#########################################################################################
import unittest, os


def bitSwapRequire(a, b):
    count = 0
    c = a ^ b  # 1s is bitwisted position
    while c != 0:
        c = c & (c - 1)  # erase the least significant bit in c
        count += 1
    return count


class bitSwapRequire_test(unittest.TestCase):
    def test(self):
        number1 = 14  # abcd1110
        number2 = 5  # abcd0101
        # abcd1011 (14 XOR 5 is 11)
        print(bitSwapRequire(number1, number2))
        os.system("Pause")


unittest.main()
