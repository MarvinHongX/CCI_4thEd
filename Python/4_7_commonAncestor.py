# commonAncestor.py
#########################################################################################
# Author  : Hong
# Created : 14/11/2017
# Modified: 15/11/2017
# Notes   : [4.7] Design an algorithm and write code to find the first common ancestor of two nodes
#                in a binary tree. Avoid storing additional nodes in a data structure.
#                NOTE: This is not necessarily a binary search tree.
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
        if val > node.value:
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


class Result:
    def __init__(self, tree, isAnc):
        self.node = tree
        self.isAncestor = isAnc


def commonAncestorHelper(root, node1, node2):
    if root == None:
        return Result(None, False)

    if root == node1 and root == node2:
        return Result(root, True)

    rx = commonAncestorHelper(root.left, node1, node2)
    if rx.isAncestor:  # found common ancestor
        return rx

    ry = commonAncestorHelper(root.right, node1, node2)
    if ry.isAncestor:  # found common ancestor
        return ry

    if rx.node != None and ry.node != Node:
        return Result(root, True)  # This is common ancestor
    elif root == node1 or root == node2:
        isAncestor = True if rx.node != None or ry.node != None else False
        return Result(root, isAncestor)
    else:
        return Result(rx.node if rx.node != None else ry.node, False)


def commonAncestor(root, node1, node2):
    r = commonAncestorHelper(root, node1, node2)
    if r.isAncestor:
        return r.node
    else:
        return None


class commonAncestor_test(unittest.TestCase):
    def test(self):
        t1 = Tree()
        t1.add(5)
        t1.add(1)
        t1.add(-1)
        t1.add(2)
        t1.add(7)
        t1.add(6)
        t1.add(8)
        res = commonAncestor(t1.root, t1.find(1), t1.find(7))
        print(res.value)
        os.system("Pause")


unittest.main()
