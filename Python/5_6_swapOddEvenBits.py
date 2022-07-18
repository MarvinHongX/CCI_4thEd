# swapOddEvenBits.py
#########################################################################################
# Author  : Hong
# Created : 24/11/2017
# Modified: 24/11/2017
# Notes   : [5.6] Write a program to swap odd and even bits in an integer with as few instructions as
#                possible (e.g., bit 0 and bit! are swapped, bit 2 and bit 3 are swapped, and so on).
#########################################################################################
import unittest, os


def swapOddEvenBits(x):
    return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)


class swapOddEvenBits_test(unittest.TestCase):
    def test(self):
        number = 13
        print(swapOddEvenBits(number))
        os.system("Pause")


unittest.main()
