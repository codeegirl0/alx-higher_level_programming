#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase of  max_integer."""

    def test_regular(self):
        """Test with regular list """
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with  non-ints list """
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """Test with an empty return none"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with negative value list"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with list mixed """
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with  parameter"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test list of one int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """return the value"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """return first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """show a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
