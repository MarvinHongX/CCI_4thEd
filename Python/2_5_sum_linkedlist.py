# sum_linkedlist.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [2.5] You have two numbers represented by a linked list, where each node contains a
#                single digit. The digits are stored in reverse order, such that the 1's digit is at the head
#                of the list. Write a function that adds the two numbers and returns the sum as a linked list.
#                FOLLOW UP
#                Suppose the digits are stored in forward order. Repeat the above problem.
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

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res

    def getHead(self):
        return self.head


def solution(list1, list2):
    v1 = list1.getHead()
    v2 = list2.getHead()
    carry = 0
    while v1 is not None:
        val = ((v1.val + v2.val) % 10) + carry  # %: remainder
        carry = (v1.val + v2.val) // 10  # //: quotient operation
        v1.val = val
        v1 = v1.next
        v2 = v2.next

    cur = list1.getHead()
    val = 0
    mul = 1
    while cur is not None:
        val = val + (cur.val * mul)
        mul = mul * 10
        cur = cur.next

    return val


def solution2(list1, list2):
    v1 = list1.getHead()
    v2 = list2.getHead()
    carry = 0
    mul = 1
    val = 0
    while v1 is not None:
        val += (v1.val + v2.val) * mul
        mul = mul * 10
        v1 = v1.next
        v2 = v2.next
    return val


class sum_linkedlist_test(unittest.TestCase):
    def test(self):
        e1 = LinkedList(5)
        e1.add(4)
        e1.add(3)
        e2 = LinkedList(8)
        e2.add(7)
        e2.add(6)
        print(id(e1))
        print(id(e2))
        print(e1.printlist())
        print(e2.printlist())
        print(id(e1))
        print(id(e2))

        print(solution2(e1, e2))
        os.system("Pause")


unittest.main()
