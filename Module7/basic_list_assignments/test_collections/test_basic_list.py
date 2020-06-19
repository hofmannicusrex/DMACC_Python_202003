"""
Program: test_string_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/18/2020

Program specifications: Tester program for basic_list.py.
"""
import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as test_basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.get_input', return_value='666')
    def test_make_list(self, input):
        self.assertEqual(test_basic_list.make_list(), [666, 666, 666])


if __name__ == '__main__':
    unittest.main()
