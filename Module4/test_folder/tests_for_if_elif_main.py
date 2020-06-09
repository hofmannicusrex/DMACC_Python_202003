"""
Program: tests_for_if_elif_main.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/8/2020

Program specifications: Test program for the if_elif_main.py program.
"""
import unittest
import unittest.mock as mock
# from the 'basic_if_elif_statements_hofmann' folder, import the 'if_elif_main' method as 'test_membership_lvl'
from basic_if_elif_statements_hofmann import if_elif_main as test_membership_lvl


class IfElifTestCases(unittest.TestCase):
    # Testing to see if the user input of 'Platinum' matches with 'Platinum'.

    def test_user_input_platinum_true(self):  # Testing for 'Platinum' == 'Platinum'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Platinum'), 'Platinum')

    def test_user_input_platinum_false(self):  # Testing for 'Platinum' == 'platinum'
        self.assertFalse(test_membership_lvl.determine_membership_lvl(user_input='Platinum'), 'platinum')

    def test_user_input_gold_true(self):  # Testing for 'Gold' == 'Gold'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Gold'), 'Gold')

    def test_user_input_gold_false(self):  # Testing for 'Gold' == 'gold'
        self.assertFalse(test_membership_lvl.determine_membership_lvl(user_input='Gold'), 'gold')

    def test_user_input_silver_true(self):  # Testing for 'Silver' == 'Silver'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Silver'), 'Silver')

    def test_user_input_silver_false(self):  # Testing for 'Silver' == 'silver'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Silver'), 'silver')

    def test_user_input_bronze_true(self):  # Testing for 'Bronze' == 'Bronze'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Bronze'), 'Bronze')

    def test_user_input_bronze_false(self):  # Testing for 'Bronze' == 'bronze'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Bronze'), 'bronze')

    def test_user_input_free_trial_true(self):  # Testing for 'Free Trial' == 'Free Trial'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Free Trial'), 'Free Trial')

    def test_user_input_free_trial_false(self):  # Testing for 'Free Trial' == 'Free trial'
        self.assertEqual(test_membership_lvl.determine_membership_lvl(user_input='Free Trial'), 'Free trial')


if __name__ == '__main__':
    unittest.main()
