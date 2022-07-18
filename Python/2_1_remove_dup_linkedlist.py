# remove_dup_linkedlist.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [2.1] Write code to remove duplicates from an unsorted linked list.
#                FOLLOW UP
#                How would you solve this problem if a temporary buffer is not allowed?
#########################################################################################
import unittest, os


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None  # next node pointer


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)  # declare head node

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def delete_duplicate(self):
        cur = self.head
        dict = {}
        prev = None
        while cur is not None:
            if cur.val in dict:
                prev.next = cur.next
            else:
                dict[cur.val] = True
                prev = cur
            cur = cur.next

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)


class remove_dup_linkedlist_test(unittest.TestCase):
    def test(self):
        e = LinkedList(4)
        e.add(4)
        e.add(5)
        e.add(6)
        e.add(4)
        e.add(7)
        e.add(4)
        e.add(6)
        e.add(6)
        e.delete_duplicate()
        self.assertEqual("[4, 5, 6, 7]", e.printlist())
        print(e.printlist())
        os.system("Pause")


unittest.main()

