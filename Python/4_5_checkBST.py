# checkBST.py
#########################################################################################
# Author  : Hong
# Created : 14/11/2017
# Modified: 14/11/2017
# Notes   : [4.5] Impement a function to check if a binary tree is a binary search tree.
#########################################################################################
import unittest, os, sys


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

    def add_error(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add_error(val, self.root)

    def _add_error(self, val, node):
        if node.left != None:
            self._add_error(val, node.left)
        else:
            node.left = Node(val)


def checkBST(tree):
    return _checkBST(tree.root, -sys.maxsize - 1, sys.maxsize)


def _checkBST(node, min, max):
    if node is None:
        return True
    if node.value <= min or node.value > max:
        return False
    if _checkBST(node.left, min, node.value) == False or _checkBST(node.right, node.value, max) == False:
        return False
    return True


class checkBST_test(unittest.TestCase):
    def test(self):
        n = Tree()
        n.add(1)
        n.add(2)
        n.add(3)
        n.add_error(4)  # not a binary tree since 4 is in the wrong place
        print(checkBST(n))
        os.system("Pause")


unittest.main()
