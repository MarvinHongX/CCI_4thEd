# binaryTree_balance.py
#########################################################################################
# Author  : Hong
# Created : 10/11/2017
# Modified: 10/11/2017
# Notes   : [4.1] Implement a function to check if a binary tree is balanced. For the purposes of this
#                 question, a balanced tree is defined to be a tree such that the heights of the two
#                 subtrees of any node never differ by more than one.
#########################################################################################
import unittest, os, math


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root == None):
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

    def find(self, val):
        if self.root != None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left != None:
            return self._find(val, node.left)
        elif val > node.value and node.right != None:
            return self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(str(node.value) + ' ')
            self._printTree(node.right)

    def checkHeight(self, node):
        if node is None:
            return 0  # Height of 0

        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1  # Not balanced

        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1  # Not balanced

        heightDiff = leftHeight - rightHeight
        if abs(heightDiff) > 1:
            return -1  # Not balanced
        else:
            if self.root == node and heightDiff != 0:
                return -1  # Not balance
            else:
                return max(leftHeight, rightHeight) + 1

    def isBalanced(self):
        if self.checkHeight(self.root) == -1:
            return False
        else:
            return True


class binaryTree_balance_test(unittest.TestCase):
    def test(self):
        tree = Tree()
        tree.add(3)
        print(tree.isBalanced())
        tree.add(4)
        print(tree.isBalanced())
        tree.add(0)
        print(tree.isBalanced())
        tree.add(8)
        print(tree.isBalanced())
        tree.add(2)
        print(tree.isBalanced())
        tree.printTree()
        print(tree.isBalanced())

        print(tree.find(3).value)
        print(tree.find(10))
        tree.deleteTree()
        tree.printTree()
        os.system("Pause")


unittest.main()
