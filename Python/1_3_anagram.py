# anagram.py
########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.3] Given two strings, write a method to decide if one is a permutation of
#                the other
#########################################################################################

import unittest, os


def anagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False


class anagramTest(unittest.TestCase):
    def test(slef):
        # self.assertTrue(anagram("elvis","livez"))
        print(anagram("elvis", "lives"))
        # self.assertTrue(anagram("basic","is abd"))
        print(anagram("basic", "is abd"))
        print(anagram("ba1", "1ab"))
        os.system("Pause")


unittest.main()
