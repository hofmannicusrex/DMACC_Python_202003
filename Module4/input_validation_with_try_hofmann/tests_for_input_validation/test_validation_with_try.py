"""
Program: test_validation_with_try.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/9/2020

Program specifications: The program will.
"""
import unittest
from input_validation_main import validation_with_try as calc_average_main


def test_average_exception(self):
    with self.assertRaises(ValueError):
        calc_average_main.calculate_average(-1, 1, 1)
