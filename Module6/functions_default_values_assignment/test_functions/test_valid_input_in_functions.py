"""
Program: test_valid_input_in_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/17/2020

Program specifications: Tester program for validate_input_in_functions.py.
"""
import unittest
import more_functions.validate_input_in_functions as test_score_input


class MyTestCase(unittest.TestCase):

    def test_score_input(self):
        self.assertEqual('Nick Hofmann: 97', test_score_input.score_input('Nick Hofmann', 97))
