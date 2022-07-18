# stack_min.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [3.2] How would you design a stack which, in addition to push and pop, also has a
#                function min which returns the minimum element? Push, pop and min should all
#                operate in 0(1) time.
#########################################################################################
import unittest, os


class stack():
    def __init__(self):
        self.items = []
        self.mins = []
        self.min = None

    def push(self, item):
        self.items.append(item)
        if self.min is not None:
            self.mins.append(self.min)  # stack on mins
        if self.min is None or self.min > item:
            self.min = item

    def pop(self):
        self.items.pop()
        if len(self.mins) > 0:
            self.min = self.mins.pop()
        else:
            self.min = None

    def getMinimum(self):
        return self.min

    def peak(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None


class stack_min_test(unittest.TestCase):
    def test(self):
        stc = stack()
        stc.push(4)
        stc.push(3)
        stc.push(2)
        print(stc.getMinimum())
        print(stc.peak())

        stc.push(-8)
        print(stc.getMinimum())
        print(stc.peak())

        stc.pop()
        print(stc.getMinimum())
        print(stc.peak())

        stc.pop()
        print(stc.getMinimum())
        print(stc.peak())

        stc.pop()
        print(stc.getMinimum())
        print(stc.peak())

        stc.pop()
        print(stc.getMinimum())
        print(stc.peak())

        os.system("Pause")


unittest.main()
