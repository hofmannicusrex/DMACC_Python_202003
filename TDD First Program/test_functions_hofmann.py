"""
Program: test_functions_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/3/2020


Program specifications: The program will have will prompt for the age of one infant (age 1-5 years)
who is attending camp and convert the age in months to years via a function call then print the result.

Write a program camper_age_input.py with a main function. (Name is important! If you are programming
tasked with writing a script called x, and you call it y, other part of the program expecting x cannot
 run your code.)

Your computer is performing all four functions 1. store and input, 2. process and store, 3. output.
More specifically

1.Store a numeric value in a variable age_in_years from input

2.Perform calculation, store answer in a variable age_in_months use symbolic constant years to
months conversion (in a function call convert_to_months()) that returns the value

3.Output the answer variable received from the function with meaning string to inform the user what
the output means
"""

import unittest
from camper_age_input_hofmann import camper_age_input_hofmann


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(360, camper_age_input_hofmann.convert_to_months(30))  # Good age range (in years): 3-72


if __name__ == '__main__':
    unittest.main()

