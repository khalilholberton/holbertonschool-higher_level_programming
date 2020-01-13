#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    This class contains test methods for max_integer(list=[])
    '''
    def test_correct_output(self):
        '''passing valid list
        '''
        self.assertEqual(max_integer([30, 4, 27, 9]), 30)
        self.assertEqual(max_integer([2, 7, 8, 1]), 8)
        self.assertEqual(max_integer([66, 89]), 89)

    def test_negative_positive_integers(self):
        '''passing list with negatives and positives integers
        '''
        self.assertEqual(max_integer([-3, 5, -99, 1, -897]), 5)

    def test_empty_list(self):
        '''passing list with no elements
        '''
        self.assertEqual(max_integer([]), None)

    def test_no_list(self):
        '''passing no argument
        '''
        self.assertEqual(max_integer(), None)

    def test_integers_string(self):
        '''passing list with integers and string
        '''
        with self.assertRaises(TypeError):
            max_integer(["khalil", 9, 1, 7])
