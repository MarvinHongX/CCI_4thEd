# isUniqChar.py
#########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.1] Implement an algorithm to determine if a string has all unique characters.
#                What if you cannot use additional data structures?
#                (We'll assume that the character set is ASCII not Unicode string.)
#########################################################################################


def isUniqChar(str):  # list
    if (len(str) > 256):
        return False

    hash = [False] * 256  # 0~255

    for ch in str:
        if (hash[ord(ch)]) is True:  # ord(): Characters to ASCII
            return False
        else:
            hash[ord(ch)] = True
    return True


def isUniqChar2(str):  # Bitwise operation
    if (len(str) > 256):
        return False

    checker = 0

    for i in range(0, len(str)):
        val = ord(str[i]) - ord('a')
        if ((checker & (1 << val)) > 0):  # expression1 << expression2:
            return False
        else:
            checker |= (1 << val)
    return True


def isUniqCharResult(result):
    if (result):
        print("Duplicate Characters Not Exist.")
    else:
        print("Duplicate Characters Exist.")


if __name__ == '__main__':
    isUniqCharResult(isUniqChar("abcda"))
    isUniqCharResult(isUniqChar("abcde"))
    isUniqCharResult(isUniqChar("apple"))

    isUniqCharResult(isUniqChar2("abcda"))
    isUniqCharResult(isUniqChar2("abcde"))
    isUniqCharResult(isUniqChar2("apple"))
