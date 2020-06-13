"""
Program: coupon_calculations.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/12/2020

Program specifications: The program will calculate the total cost of the order based off of
three user inputs: sticker price of the item, value of their cash coupon, and amount of their
percent coupon.
"""
import constants as const


def calculate_price(price, cash_coupon, percent_coupon):

    price_after_cash_coupon = price - cash_coupon

    # Do I have a cash coupon? How does that affect the outcome?
    # Do I have a discount? HOw does that affect the outcome?
    # What is the shipping cost? How can I calculate that/add it in?
    # Using the outer if statement to determine the shipping cost since it's based off of the init. price - cash_coupon
    if 0 <= price_after_cash_coupon < const.TEN_DOLLAR_THRESHOLD:  # if 0 <= price_after_cash_coupon < 10

        if percent_coupon == 10:  # AND percent_coupon is 10%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_10) + const.UNDER_10_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 15:  # AND percent_coupon is 15%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_15) + const.UNDER_10_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 20:  # AND percent_coupon is 20%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_20) + const.UNDER_10_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

    elif const.TEN_DOLLAR_THRESHOLD <= price_after_cash_coupon < const.THIRTY_DOLLAR_THRESHOLD:  # if 10 <= price_after_cash_coupon < 30

        if percent_coupon == 10:  # AND percent_coupon is 10%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_10) + const.BETWEEN_10_TO_30_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 15:  # AND percent_coupon is 15%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_15) + const.BETWEEN_10_TO_30_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 20:  # AND percent_coupon is 20%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_20) + const.BETWEEN_10_TO_30_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

    elif const.THIRTY_DOLLAR_THRESHOLD <= price_after_cash_coupon < const.FIFTY_DOLLAR_THRESHOLD:  # if 30 <= price_after_cash_coupon < 50

        if percent_coupon == 10:  # AND percent_coupon is 10%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_10) + const.BETWEEN_30_TO_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 15:  # AND percent_coupon is 15%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_15) + const.BETWEEN_30_TO_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 20:  # AND percent_coupon is 20%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_20) + const.BETWEEN_30_TO_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

    elif price_after_cash_coupon > const.FIFTY_DOLLAR_THRESHOLD:  # if price_after_cash_coupon > 50

        if percent_coupon == 10:  # AND percent_coupon is 10%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_10) + const.OVER_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 15:  # AND percent_coupon is 15%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_15) + const.OVER_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

        elif percent_coupon == 20:  # AND percent_coupon is 20%
            final_price = ((price_after_cash_coupon * const.PERCENT_COUPON_20) + const.OVER_50_SHIPPING) * const.SALES_TAX_RATE
            print('\nThe final order price is: ', '${:,.2f}'.format(final_price))

    else:
        print('\nWe\'re sorry but your total order price cannot be a negative dollar amount. Please try again.')

    # Outer if - elif statement for price variable ranges
    #       Inner if - elif statements in each of those 4 price ranges?

    # IF STATEMENT MAY ONLY BE 12 OR 13 LINES ACCORDING TO PROFESSOR

    # Subtotal, now add tax.
    # return your total value


if __name__ == '__main__':
    price = float(input('What is the sticker or initial price of the item? '))
    cash_coupon = float(int(input('What kind of cash coupon do you have? ($5 or $10) ')))
    percent_coupon = float(int(input('What is the amount of your percent coupon? (10%, 15%, 20%) ')))

    calculate_price(price, cash_coupon, percent_coupon)
