# list_of_stack.py
#########################################################################################
# Author  : Hong
# Created : 8/11/2017
# Modified: 8/11/2017
# Notes   : [3.3] Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
#                in real life, we would likely start a new stack when the previous stack exceeds some
#                threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
#                Stacks should be composed of several stacks and should create a new stack once
#                the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.
#                pop() should behave identically to a single stack (that is, pop() should return the
#                same values as it would if there were just a single stack).
#                FOLLOW UP
#                Implement a function popAt(int index) which performs a pop operation on a
#                specific sub-stack.
#########################################################################################
import unittest, os


class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Stacks():
    def __init__(self):
        self.stacklist = []
        self.max_stack_size = 3
        self.stacklist.append(Stack())

    def push(self, item):
        st = self.getLastStack()
        if self.max_stack_size == st.size():
            new_st = Stack()
            new_st.push(item)
            self.stacklist.append(new_st)
        else:
            st.push(item)

    def pop(self):
        st = self.getLastStack()
        if st.is_empty():
            self.stacklist.pop()
            st = self.getLastStack()
            st.pop()
        else:
            st.pop()

    def getLastStack(self):
        return self.stacklist[len(self.stacklist) - 1]

    def getStacksCount(self):
        return len(self.stacklist)

    def printStacks(self):
        result = []
        for st in self.stacklist:
            for item in st.items:
                result.append(item)
        return result


class list_of_stack_test(unittest.TestCase):
    def test(self):
        sts = Stacks()
        sts.push(5)
        sts.push(3)
        sts.push(2)
        sts.push(2)
        sts.push(1)
        sts.push(1)
        sts.push(7)
        sts.push(8)
        sts.push(9)
        sts.push(10)
        print(sts)
        print(sts.printStacks())
        print(sts.getStacksCount())
        sts.pop()
        print(sts)
        print(sts.printStacks())
        print(sts.getStacksCount())
        sts.pop()
        print(sts)
        print(sts.printStacks())
        print(sts.getStacksCount())
        os.system("Pause")


unittest.main()


