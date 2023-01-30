#!/usr/bin/python3
"""Testing for max_integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class MaxIntTest(unittest.TestCase):

    def max_int_test(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-5, -9, 0, -4]), 0)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)

    def test_max_boolean(self):
        self.assertTrue(max_integer([True, False]), True)

    def max_string_test(self):
        self.assertEqual(max_integer(["hello world"]), "hello world")
