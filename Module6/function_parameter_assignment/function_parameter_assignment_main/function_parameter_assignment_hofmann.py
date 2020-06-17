"""
Program: function_parameter_assignment_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/16/2020

Program specifications: The program will demonstrate a basic function
with parameters.
"""


def multiply_string(message, n):
    """
    :param message: String containing my favorite class this semester.
    :param n: Int containing the number of times I want the message to print.
    :return: The string * the int.
    """
    return print(message * n)


if __name__ == '__main__':
    multiply_string('C++\t', 6)
