# findMissing.py
#########################################################################################
# Author  : Hong
# Created : 24/11/2017
# Modified: 27/11/2017
# Notes   : [5.7] An array A contains all the integers from 0 through n, except for one number which is
#                missing. In this problem, we cannot access an entire integer in A with a single operation.
#                The elements of A are represented in binary, and the only operation we can use
#                to access them is "fetch the jth bit of A[i]" which takes constant time. Write code to
#                find the missing integer. Can you do it in 0(n) time?
#########################################################################################
import unittest, os


def findMissing(array):
    # start from the least significant bit, and work our way up
    return _findMissing(array, 0)


def _findMissing(input, column):
    if len(input) == 0 or column > len(input[len(input) - 1]) - 2:  # we're done
        return 0

    oneBits = []
    zeroBits = []

    for t in input:
        i = column + 1
        if len(t) - 2 >= i:
            s = t[-i]
            if t[-i] == '0':
                zeroBits.append(t)
            else:
                oneBits.append(t)
        else:
            zeroBits.append(t)
    if len(zeroBits) <= len(oneBits):
        v = _findMissing(zeroBits, column + 1)
        return (v << 1) | 0
    else:
        v = _findMissing(oneBits, column + 1)
        return (v << 1) | 1


class findMissing_test(unittest.TestCase):
    def test(self):
        ar = []
        n = 10
        for i in range(0, n + 1):
            ar.append(bin(i))

        del ar[5]

        print(findMissing(ar))
        os.system("Pause")


unittest.main()
