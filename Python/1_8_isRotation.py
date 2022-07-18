# isRotation.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [1.8] Assume you have a method isSubstring which checks if one word is a substring
#                of another. Given two strings, s1 and s2, write code to check If s2 is a rotation of s1
#                using only onecalltoisSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
#########################################################################################
import unittest, os, string, random, copy


def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1

        return s2 in s1s1  # isSubstring
    return false


class isRotation_test(unittest.TestCase):
    def test(self):
        s1 = "isRotation"
        s2 = "Rotationis"
        print(isRotation(s1, s2))
        os.system("Pause")


unittest.main()
