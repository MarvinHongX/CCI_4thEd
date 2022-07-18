# rotate.py
#########################################################################################
# Author  : Hong
# Created : 7/11/2017
# Modified: 7/11/2017
# Notes   : [1.6] Given an image represented by an NxN matrix, where each pixel in the image is 4
#                bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
#########################################################################################
import unittest, os, string, random, copy


def rotate(matrix):  # Clockwise 90
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for i in range(m)]  # m by n matrix
    for i in range(0, n):
        for j in range(0, m):
            # result[j][i] = matrix[i][j] #transpose
            result[j][n - 1 - i] = matrix[i][j]

    return result


def rotate2(matrix):  # Counter-clockwise
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for i in range(m)]  # m by n matrix
    for i in range(0, n):
        for j in range(0, m):
            result[m - 1 - j][i] = matrix[i][j]
    return result


class rotate_test(unittest.TestCase):
    def test(self):
        n = 3
        m = 2
        A = [[0] * m for i in range(n)]  # n by m matrix

        for j in range(0, m):  # 0 ~ m-1
            for i in range(0, n):  # 0 ~ n-1
                A[i][j] = random.randint(0, 100)  # random integer
        print(A)
        print(rotate(A))
        print(rotate2(A))
        os.system("Pause")


unittest.main()
