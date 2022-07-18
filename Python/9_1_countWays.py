# countWays.py
#########################################################################################
# Author  : Hong
# Created : 28/11/2017
# Modified: 28/11/2017
# Notes   : [9.1] A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or
#                3 steps at a time. Implement a method to count how many possible ways the child
#                can run up the stairs.
#########################################################################################
import unittest, os, functools


def memoize(f):
    cache = {}

    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, fkwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]

    return memf


@memoize
def countWays(steps, max_steps=3):
    """ Return in how many possible ways we can run up the stairs """
    if not steps:
        return 1
    elif steps < 0:
        return 0
    else:
        total = 0
        for n in range(1, min(steps, max_steps) + 1):
            total += countWays(steps - n, max_steps=max_steps)
        return total


class countWays_test(unittest.TestCase):
    def test(self):
        self.assertEqual(countWays(1), 1)
        self.assertEqual(countWays(2), 2)  # (1 + 1) or (2)
        self.assertEqual(countWays(3), 4)  # (1 + 1) or (2 + 1) or (1 + 2) or (3)
        self.assertEqual(countWays(4), 7)
        self.assertEqual(countWays(5), 13)
        self.assertEqual(countWays(6), 24)
        self.assertEqual(countWays(7), 44)
        self.assertEqual(countWays(8), 81)
        self.assertEqual(countWays(9), 149)
        self.assertEqual(countWays(10), 274)
        self.assertEqual(countWays(11), 504)
        self.assertEqual(countWays(12), 927)
        self.assertEqual(countWays(13), 1705)
        self.assertEqual(countWays(14), 3136)
        self.assertEqual(countWays(15), 5768)
        self.assertEqual(countWays(16), 10609)
        self.assertEqual(countWays(17), 19513)
        self.assertEqual(countWays(18), 35890)
        self.assertEqual(countWays(19), 66012)
        self.assertEqual(countWays(20), 121415)
        self.assertEqual(countWays(21), 223317)
        self.assertEqual(countWays(22), 410744)
        self.assertEqual(countWays(23), 755476)
        self.assertEqual(countWays(24), 1389537)
        self.assertEqual(countWays(25), 2555757)
        self.assertEqual(countWays(26), 4700770)
        self.assertEqual(countWays(27), 8646064)
        self.assertEqual(countWays(28), 15902591)
        self.assertEqual(countWays(29), 29249425)
        self.assertEqual(countWays(30), 53798080)
        os.system("Pause")


if __name__ == "__main__":
    unittest.main()

