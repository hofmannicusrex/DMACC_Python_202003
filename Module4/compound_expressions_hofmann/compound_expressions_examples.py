"""
Program: compound_expressions_examples.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/8/2020

Program specifications: The program will demonstrate the use of compound expressions.
"""

if __name__ == '__main__':
    MAX = 10
    MIN = 0
    y = 5
    x = 7

    if y > MAX:
        print(y, 'is greater than', MAX)

    if y < MIN:
        print(y, 'is less than', MIN)

    if (MIN < x < MAX) and (MIN != x or x != MAX):
        print(x, 'is between', MIN, 'and', MAX, 'but is not equal to either', MAX, 'or', MIN)

    if (MIN < x < MAX) and (x != MAX):
        print(x, 'is between', MAX, 'and', MIN, 'but is not equal to', MAX)

    if MIN < x <= MAX:
        print(x, 'is greater than', MIN, 'and less than or equal to', MAX)
