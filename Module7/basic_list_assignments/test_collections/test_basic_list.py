"""
Program: test_string_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/20/2020

Program specifications: Tester program for basic_list.py.
"""
import unittest
import unittest.mock as mock_input
from unittest.mock import patch
from fun_with_collections import basic_list as test_basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='666')
    def test_make_list(self, users_input):
        self.assertEqual(test_basic_list.make_list(), [666, 666, 666])


if __name__ == '__main__':
    unittest.main()
