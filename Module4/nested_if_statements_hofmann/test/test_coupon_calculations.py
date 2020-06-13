"""
Program: test_coupon_calculations.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/12/2020

Program specifications: The program will test coupon_calculations.py.
"""
import unittest
import unittest.mock as mock
from store import coupon_calculations as coupon_calc


class MyTestCase(unittest.TestCase):
    # def calculate_price(price, cash_coupon, percent_coupon):
    def test_price_under_ten(self):  # Test at the low and high sides of the range
        price_under_10_1 = 7.99
        price_under_10_2 = 1.12
        # Tests for the value of price_under_10_1
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 5, 10), 9.16, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 5, 15), 9, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 5, 20), 8.84, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 10, 10), 4.39, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 10, 15), 4.5, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_1, 10, 20), 4.6, places=2)
        # Tests for the value of price_under_10_2
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 5, 10), 2.61, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 5, 15), 2.81, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 5, 20), 3.02, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 10, 10), -2.16, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 10, 15), -1.69, places=2)
        self.assertAlmostEqual(coupon_calc.calculate_price(price_under_10_2, 10, 20), -1.22, places=2)

        #     def test_price_ten_to_thirty(self):
        #         price_between_10_and_30 = 6.90
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_10_and_30, 5, 10), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_10_and_30, 5, 15), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_10_and_30, 5, 20), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_10_and_30, 10, 10), 9.48, places=4)
        #
        #     def test_price_thirty_to_fifty(self):
        #         price_between_30_and_50 = 6.90
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_30_and_50, 5, 10), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_30_and_50, 5, 15), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_30_and_50, 5, 20), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_between_30_and_50, 10, 10), 9.48, places=4)
        #
        #     def test_price_over_fifty(self):
        #         price_over_50 = 566.90
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_over_50, 5, 10), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_over_50, 5, 15), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_over_50, 5, 20), 9.48, places=4)
        #         self.assertAlmostEqual(coupon_calc.calculate_price(price_over_50, 10, 10), 9.48, places=4)


if __name__ == '__main__':
    unittest.main()
