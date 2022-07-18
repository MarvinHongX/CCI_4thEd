# encode_space.py
########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.4] Write a method to replace all spaces in a string with'%20'. You may assume that
#                the string has sufficient space at the end of the string to hold the additional
#                characters, and that you are given the "true" length of the string.
#                (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
#                EXAMPLE
#                Input: "Mr John Smith"
#                Output: "Mr%20Dohn%20Smith"
#########################################################################################
import unittest, os


def encode_space(str):
    return str.strip().replace(" ", "%20")
    # return str.replace(" ","%20")


class encode_space_test(unittest.TestCase):
    def test(self):
        print(encode_space("How you do? "))
        os.system("Pause")


unittest.main()


