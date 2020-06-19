"""
Program: test_valid_input_in_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/17/2020

Program specifications: Tester program for validate_input_in_functions.py.
"""
import unittest
import unittest.mock as mock_user_input
import more_functions.validate_input_in_functions as test_score_input


class MyTestCase(unittest.TestCase):

    def test_score_input_test_name(self):
        self.assertEqual('\nNick Hofmann: 0%', test_score_input.score_input('Nick Hofmann'))

    def test_score_input_test_score_valid(self):
        self.assertEqual('\nNick Hofmann: 97%', test_score_input.score_input('Nick Hofmann', 97))

    def test_score_input_test_score_below_range(self):
        with mock_user_input.patch('builtins.input', side_effect=['Nick Hofmann', -1, -102, -5, 78]):
            self.assertEqual('\nNick Hofmann: 78%', test_score_input.score_input('Nick Hofmann', 78))

    def test_score_input_test_score_above_range(self):
        with mock_user_input.patch('builtins.input', side_effect=[666, 100]):
            self.assertEqual('\nNick: 100%', test_score_input.score_input('Nick', 100))

    def test_score_input_test_score_non_numeric(self):
        with mock_user_input.patch('builtins.input', side_effect=[]):
            self.assertEqual(ValueError, test_score_input.score_input('Nick Hofmann', 'non numeric'))

    def test_score_input_test_invalid_message(self):
        self.assertEqual('\nNick Hofmann: 95%', test_score_input.score_input('Nick Hofmann', 95, invalid_message='WRONG '))


if __name__ == '__main__':
    unittest.main()
