"""
Program: test_string_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/16/2020

Program specifications: Tester program for string_functions.py.
"""
import unittest
import more_functions.string_functions as test_multiply_string


class MyTestCase(unittest.TestCase):

    def test_multiple_string(self):
        self.assertEqual('NickNickNickNick', test_multiply_string.multiply_string('Nick', 4))
        self.assertEqual('OliverOliverOliverOliver', test_multiply_string.multiply_string('Oliver', 4))


if __name__ == '__main__':
    unittest.main()
