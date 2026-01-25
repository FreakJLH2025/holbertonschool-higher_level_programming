#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)
    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_all_negative(self):
        self.assertEqual(max_integer([-5, -9, -1, -3]), -1)
    def test_repeated_max(self):
        self.assertEqual(max_integer([2, 3, 3, 1]), 3)
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
