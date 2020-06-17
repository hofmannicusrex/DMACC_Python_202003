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
        self.assertEqual('Nick', test_multiply_string.multiply_string('Nick', 1))
        self.assertEqual('NickNick', test_multiply_string.multiply_string('Nick', 2))
        self.assertEqual('NickNickNick', test_multiply_string.multiply_string('Nick', 3))
        self.assertEqual('NickNickNickNick', test_multiply_string.multiply_string('Nick', 4))
        self.assertEqual('NickNickNickNickNick', test_multiply_string.multiply_string('Nick', 5))
        self.assertEqual('NickNickNickNickNickNick', test_multiply_string.multiply_string('Nick', 6))
        self.assertEqual('NickNickNickNickNickNickNick', test_multiply_string.multiply_string('Nick', 7))
        self.assertEqual('NickNickNickNickNickNickNickNick', test_multiply_string.multiply_string('Nick', 8))
        self.assertEqual('NickNickNickNickNickNickNickNickNick', test_multiply_string.multiply_string('Nick', 9))

    def test_multiple_string_2(self):
        self.assertEqual('NOCH', test_multiply_string.multiply_string('NOCH', 1))
        self.assertEqual('NOCHNOCH', test_multiply_string.multiply_string('NOCH', 2))
        self.assertEqual('NOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 3))
        self.assertEqual('NOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 4))
        self.assertEqual('NOCHNOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 5))
        self.assertEqual('NOCHNOCHNOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 6))
        self.assertEqual('NOCHNOCHNOCHNOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 7))
        self.assertEqual('NOCHNOCHNOCHNOCHNOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 8))
        self.assertEqual('NOCHNOCHNOCHNOCHNOCHNOCHNOCHNOCHNOCH', test_multiply_string.multiply_string('NOCH', 9))


if __name__ == '__main__':
    unittest.main()
