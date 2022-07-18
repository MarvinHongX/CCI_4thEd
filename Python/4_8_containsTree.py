# containsTree.py
#########################################################################################
# Author  : Hong
# Created : 15/11/2017
# Modified: 23/11/2017
# Notes   : [4.8] You have two very large binary trees: Tl, with millions of nodes, and T2, with
#                hundreds of nodes. Create an algorithm to decide if T2 is a subtree of Tl.
#                A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n
#                is identical to T2. That is, if you cut off the tree at node n, the two trees would be
#                identical.
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
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        elif node.value < val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)


def containsTree(tree1, tree2):
    if tree2.root is None:  # The empty tree is always a subtree
        return True
    return subTree(tree1.root, tree2.root)


def subTree(node1, node2):
    if node1 is None:
        return False  # big tree empty & subtree still not found
    if node1.value == node2.value:
        if matchTree(node1, node2):
            return True
    return subTree(node1.left, node2) or subTree(node1.right, node2)


def matchTree(node1, node2):
    if node1 is None and node2 is None:  # if both are empty
        return True  # nothing left in the subtree

    # if one, but not both, are empty
    if node1 is None or node2 is None:
        return False

    if node1.value != node2.value:
        return False  # data doesn't match
    return matchTree(node1.left, node2.left) and matchTree(node1.right, node2.right)


class containsTree_test(unittest.TestCase):
    def test(self):
        t1 = Tree()
        t1.add(1)
        t1.add(2)
        t1.add(3)
        t1.add(4)
        t2 = Tree()
        t2.add(3)
        t2.add(4)

        print(containsTree(t1, t2))
        os.system("Pause")


unittest.main()
