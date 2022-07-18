# printBinary.py
#########################################################################################
# Author  : Hong
# Created : 23/11/2017
# Modified: 23/11/2017
# Notes   : [5.2] Given a real number between 0 and 7 (e.g., 0.72) that is passed in as a double, print
#                the binary representation. If the number cannot be represented accurately in binary
#                with at most 32 characters, print "ERROR."
#########################################################################################
import unittest, os


def printBinary(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = []
    binary.append("0.")
    frac = 0.5
    while num > 0:
        if len(binary) > 32:
            return "ERROR"
            # return ''.join(binary)

        if num >= frac:
            binary.append("1")
            num -= frac
        else:
            binary.append("0")
        frac /= 2
    return ''.join(binary)


class printBinary_Test(unittest.TestCase):
    def test(self):
        print(printBinary(0.55))  # irrational number on binary
        print(printBinary(0.625))
        os.system("Pause")


unittest.main()
