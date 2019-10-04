"""
This is the test file for my stats tools functions
run this in terminal with python stats_tools_test.py
optionally you can do verbose mode by adding -v to that command
"""


import unittest
import numpy as np
from stats_tools import mean, mode, median, variance, stddev, coeffvar


list1 = [1, 1, 1, 2, 3, 3, 6, 7, 8, 9]


class StatsTests(unittest.TestCase):
    """
    Test stats_tools functions
    """

    def test_mean(self):
        """
        test mean()
        """
        self.assertEqual(float(mean(list1)), np.mean(list1))

    def test_mode(self):
        """
        test mode()
        """
        self.assertEqual(mode(list1), 1)

    def test_median(self):
        """
        test median()
        """
        self.assertEqual(median(list1), np.median(list1))

    def test_variance(self):
        """
        test variance() and variance(sample=False)
        """
        self.assertEqual(variance(list1, sample=False), np.var(list1))
        self.assertEqual(variance(list1), np.var(list1, ddof=1))

    def test_stddev(self):
        """
        test stddev() and stddev(samepl=False)
        """
        self.assertEqual(stddev(list1, sample=False), np.std(list1))
        self.assertEqual(stddev(list1), np.std(list1, ddof=1))

    def test_coeffvar(self):
        """
        test coeffvar() and coeffvar(sample=False)
        """
        self.assertEqual(coeffvar(list1, sample=False), np.std(list1) /
                         np.mean(list1))
        self.assertEqual(coeffvar(list1), np.std(list1, ddof=1) /
                         np.mean(list1))

if __name__ == '__main__':
    unittest.main()
