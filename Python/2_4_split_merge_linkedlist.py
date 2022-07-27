# split_merge_linkedlist.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [2.4] Write code to partition a linked list around a value x, such that all nodes less than x
#                come before all nodes greater than or equal to x.
#########################################################################################
import unittest, os


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class Linkedlist:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res

    def getHead(self):
        return self.head


def solution(e, key):
    cur = e.getHead()
    pre = None
    post = None

    # split

    while cur is not None:
        if cur.val != key:
            if cur.val > key:
                if post is None:
                    post = Linkedlist(cur.val)
                else:
                    post.add(cur.val)
            elif cur.val < key:
                if pre is None:
                    pre = Linkedlist(cur.val)
                else:
                    pre.add(cur.val)
        cur = cur.next
    cur = pre.getHead()

    # merge

    while cur.next is not None:
        cur = cur.next
    cur.next = Node(key)
    cur.next.next = post.getHead()
    return pre.printlist()


class split_merge_linkedlist_test(unittest.TestCase):
    def test(self):
        e = Linkedlist(4)
        e.add(-3)
        e.add(-2)
        e.add(3)
        e.add(1)
        e.add(0)
        e.add(2)
        e.add(-1)

        print(e.printlist())
        print(solution(e, 0))
        os.system("Pause")


unittest.main()
