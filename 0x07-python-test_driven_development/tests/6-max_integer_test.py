#!/usr/bin/python3
"""
Unittest for max_integer([..])

"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer"""

    def test_max_integer(self):
        """Tests for max_integer"""
        # expected input
        input = []
        self.assertEqual(max_integer(input), None)

        input = [1]
        self.assertEqual(max_integer(input), 1)

        input = [0, 1]
        self.assertEqual(max_integer(input), 1)

        input = [0, -1]
        self.assertEqual(max_integer(input), 0)

        input = [-1, -3]
        self.assertEqual(max_integer(input), -1)

        input = [1, 2, 3]
        self.assertEqual(max_integer(input), 3)

        input = [3, 2, 1]
        self.assertEqual(max_integer(input), 3)

        input = [1, 3, 2]
        self.assertEqual(max_integer(input), 3)

        # unexpected input
        input = [0.5, 0]
        self.assertEqual(max_integer(input), 0.5)

        input = [None]
        self.assertEqual(max_integer(input), None)

        input = [None, 0]
        # self.assertRaises(max_integer(input), TypeError)

        input = ['b', 0]
        # self.assertEqual(max_integer(input), 'b')

        input = ['a', 'b']
        self.assertEqual(max_integer(input), 'b')

        input = [True, False]
        self.assertEqual(max_integer(input), True)

        input = [True, 0]
        self.assertEqual(max_integer(input), True)

        input = [[1], [1, 1], [1, 1, 1]]
        self.assertEqual(max_integer(input), [1, 1, 1])

        # invalid types
        input = None
        # self.assertRaises(max_integer(input), ValueError)

        input = "Hello world"
        self.assertEqual(max_integer(input), "w")

        input = (1, 3, 2)
        self.assertEqual(max_integer(input), 3)

        input = {1, 2, 3}
        # self.assertRaises(max_integer(input), TypeError)
