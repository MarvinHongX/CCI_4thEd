# setZeros.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [1.7] Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#                column are set to 0.
#########################################################################################
import unittest, os, string, random, copy


def setZeros(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = [False for i in range(n)]
    column = [False for i in range(m)]
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                row[i] = [True]
                column[j] = [True]
    for i in range(0, n):
        for j in range(0, m):
            if (row[i] or column[j]):
                matrix[i][j] = 0

    return matrix


class setZeros_test(unittest.TestCase):
    def test(self):
        n = 4
        m = 6
        A = [[0] * m for i in range(n)]  # n by m matrix

        for j in range(0, m):
            for i in range(0, n):
                A[i][j] = random.randint(0, 9)
        print(A)
        print(setZeros(A))
        os.system("Pause")


unittest.main()
