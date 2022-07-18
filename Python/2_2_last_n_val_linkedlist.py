# last_n_val_linkedlist.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [2.2] Implement an algorithm to find the kth to last element of a singly linked list
#########################################################################################
import unittest, os


class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def delete_duplicate(self):
        cur = self.head
        prev = None
        dic = {}
        while cur is not None:
            if cur.val in dic:
                prev.next = cur.next
            else:
                dic[cur.val] = True
                prev = cur
            cur = cur.next

    def kth_element_from_last(self, k):
        p1 = self.head
        p2 = self.head
        if k != 0:
            for i in range(k):
                p2 = p2.next
            if p2 is None:
                return None
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        return p1.val

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)


class last_n_val_linkedlist_test(unittest.TestCase):
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
        print(e.printlist())
        print(e.kth_element_from_last(1))
        os.system("Pause")


unittest.main()



