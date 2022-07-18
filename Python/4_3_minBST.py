# minBST.py
#########################################################################################
# Author  : Hong
# Created : 10/11/2017
# Modified: 14/11/2017
# Notes   : [4.3] Given a sorted (increasing order) array with unique integer elements, write an algorithm
#                 to create a binary search tree with minimal height.
#########################################################################################
import unittest, os


class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left != None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right != None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(str(node.value) + ' ')
            self._printTree(node.right)


def createMinimalBST(array):
    tree = Tree()
    tree.root = _createMinimalBST(array, 0, len(array) - 1)
    return tree


def _createMinimalBST(array, start, end):
    if end < start:
        return None
    mid = round((start + end) / 2)
    n = Node(array[mid])
    n.left = _createMinimalBST(array, start, mid - 1)
    n.right = _createMinimalBST(array, mid + 1, end)
    return n


class minBST_test(unittest.TestCase):
    def test(self):
        arr = []
        arr.append(1)
        arr.append(3)
        arr.append(5)
        arr.append(6)
        arr.append(7)
        arr.append(8)

        t1 = createMinimalBST(arr)
        t1.printTree()

        t2 = Tree()
        t2.add(arr.pop())
        t2.add(arr.pop())
        t2.add(arr.pop())
        t2.add(arr.pop())
        t2.add(arr.pop())
        t2.add(arr.pop())
        t2.printTree()
        os.system("Pause")


unittest.main()

