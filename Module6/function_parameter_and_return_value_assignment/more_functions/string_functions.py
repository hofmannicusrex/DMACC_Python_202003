"""
Program: string_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/16/2020

Program specifications: The program will .
"""


def multiply_string(message, n):
    """
    :param message: Contains a string that will be multiplied by an integer.
    :param n: The integer that the string will be multiplied by.
    :return: Returns the multiplied, concatenated string.
    """
    string_return = message * n
    return string_return


if __name__ == '__main__':
    print(multiply_string('This language is confusing...it\'s supposed to be easy.\n', 15))
