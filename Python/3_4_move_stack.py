# move_stack.py
#########################################################################################
# Author  : Hong
# Created : 10/11/2017
# Modified: 10/11/2017
# Notes   : [3.4] In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
#                different sizes which can slide onto any tower. The puzzle starts with disks sorted
#                in ascending order of size from top to bottom (i.e., each disk sits on top of an even
#                larger one). You have the following constraints:
#                (1) Only one disk can be moved at a time.
#                (2) A disk is slid off the top of one tower onto the next rod.
#                (3) A disk can only be placed on top of a larger disk.
#                Write a program to move the disks from the first tower to the last using Stacks.
#                (Tower of Hanoi
#########################################################################################
import unittest, os, operator


class stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []


class Tower:
    def __init__(self, idx):
        self.index = idx
        self.disks = stack()

    def getIndex(self):
        return self.index

    def add(self, d):
        if self.disks.isEmpty() == False and self.disks.peek() <= d:
            print("Error placing disk", d)
        else:
            self.disks.add(d)

    def getDisks(self):
        return self.disks.items

    def moveTopTo(self, t):
        top = self.disks.pop()
        t.add(top)
        A = self.index
        B = t.index
        print("Move disk " + str(top) + " from " + str(A) + " to " + str(B))

    def moveDisks(self, n, destination, buffer):
        '''
           step1. to buffer (except last disk)
	    step2. last disk to destination
	    step3. to destination from buffer
        '''
        if n > 0:
            self.moveDisks(n - 1, buffer, destination)  # step1

            self.moveTopTo(destination)  # step2

            # print towers
            x = {}
            x.update({self.index: self.getDisks()})
            x.update({buffer.index: buffer.getDisks()})
            x.update({destination.index: destination.getDisks()})
            res = sorted(x.items(), key=operator.itemgetter(0))
            print(res[0][1], res[1][1], res[2][1])

            buffer.moveDisks(n - 1, destination, self)  # step3


class move_stack_test(unittest.TestCase):
    def test(self):

        n = 4
        towers = []
        for i in range(0, 3):
            towers.append(Tower(i))

        for i in range(n - 1, -1, -1):  # n-1 ~ 0
            towers[0].add(i)
        towers[0].moveDisks(n, towers[2], towers[1])

        os.system("Pause")


unittest.main()
