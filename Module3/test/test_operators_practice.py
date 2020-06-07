"""
Program: test_operators_practice.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/7/2020

Program specifications: The program will demonstrate the user of operators.
"""
import unittest


class OperatorsTest(unittest.TestCase):
    # Demonstrating '==' operator.

    def test_equals_false(self):
        self.assertFalse(65 == 75)

    def test_equals_true(self):
        self.assertTrue(1337 == 1337)

    # Demonstrating '!=' operator.

    def test_not_equals_false(self):
        self.assertFalse(65 != 75)

    def test_not_equals_true(self):
        self.assertTrue(1337 != 1337)

    # Demonstrating '>' operator.

    def test_greater_than_false(self):
        self.assertFalse(65 > 75)

    def test_greater_than_true(self):
        self.assertTrue(9000 > 1337)

    # Demonstrating '<' operator.

    def test_less_than_false(self):
        self.assertFalse(1337 < 75)

    def test_less_than_true(self):
        self.assertTrue(13 < 1337)

    # Demonstrating '>=' operator.

    def test_greater_than_or_equals_false(self):
        self.assertFalse(65 >= 75)

    def test_greater_than_or_equals_true(self):
        self.assertTrue(1337 >= 1337)

    # Demonstrating '<=' operator.

    def test_less_than_or_equals_false(self):
        self.assertFalse(695 <= 75)

    def test_less_than_or_equals_true(self):
        self.assertTrue(1337 <= 1337)


if __name__ == '__main__':
    unittest.main()
