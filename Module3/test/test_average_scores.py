"""
Program: test_average_scores.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/6/2020

Program specifications: The program will .
"""
import  unittest
import unittest.mock as mock
from Module3.format_output import average_scores as avg


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert avg.average() == 90


if __name__ == '__main__':
    unittest.main()
