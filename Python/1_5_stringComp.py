# stringComp.py
#########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.5] Implement a method to perform basic string compression using the counts
#                of repeated characters. For example, the string aabcccccaaa would become
#                a2blc5a3. If the "compressed" string would not become smaller than the original
#                string, your method should return the original string.
#########################################################################################
import unittest, os, string


def compressword(str):
    buffer = None
    result = ""
    i = 1
    for ch in str:
        if buffer is None:
            result += ch
            buffer = ch
        else:
            if buffer == ch:
                i += 1
            else:
                result += repr(i)
                i = 1
                result += ch
                buffer = ch
    result += repr(i)

    if len(result) > len(str):
        return str
    else:
        return result

    return result


class stringCompTest(unittest.TestCase):
    def test(self):
        print(compressword("abbbbccddeeeee"))
        # print(compressword("abb"))
        os.system("Pause")


unittest.main()

