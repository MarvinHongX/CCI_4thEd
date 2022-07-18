# reverseStr.py
#########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.2] Implement a function void revers(char* str) in C or C++ which reverse a
#                null-terminated string.
#########################################################################################

import unittest  # Unit testing framework
import os, string, copy


def reverseString(str):  # List
    return str[::-1]


def reverseString2(str):  # Stack(append, pop) structer
    stack = []
    for ch in str:
        stack.append(ch)

    result = ""
    while len(stack) > 0:
        result += stack.pop()

    return result


def reverseString3(str):  # Pointer
    global end
    end = copy.deepcopy(str)
    tmp = ""
    result = id(end)

    # THERE IS NO POINTER IN PYTHON
    return result


def reverseWord(str):
    return " ".join(reversed(str.split()))


def reverseWord2(str):
    return " ".join(str.split()[::-1])


def reverseWord3(str):  # Stack(append, pop) structer
    stack = []
    space = set(string.whitespace)
    i = 0
    while i < len(str):
        if str[i] not in space:
            chStart = i
            while i < len(str) and str[i] not in space:
                i += 1
            stack.append(str[chStart:i])
        i += 1
    return " ".join(reversed(stack))


def reverseWord4(str):
    stack = str[::-1].split()
    return " ".join([ch[::-1] for ch in stack])


class reverseStringTest(unittest.TestCase):
    def test(self):
        input = "abcde"
        self.assertEqual("edcba", reverseString(input))
        print(reverseString(input))

        input = "hong"
        self.assertEqual("gnoh", reverseString2(input))
        print(reverseString2(input))

        input = "Lee"
        print(reverseString3(input))
        print(id(end))

        input = "This is Python"
        print(reverseWord(input))

        input = "It is awesome"
        print(reverseWord2(input))

        input = "It is Stack"
        print(reverseWord3(input))

        input = "It is likey to do"
        print(reverseWord4(input))
        os.system("Pause")


unittest.main()

