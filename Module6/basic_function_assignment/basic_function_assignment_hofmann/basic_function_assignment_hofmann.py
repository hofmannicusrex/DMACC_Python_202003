"""
Program: basic_function_assignment_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/15/2020

Program specifications: The program will demonstrate a simple method call. It will handle
simple input errors using a try-catch statement as well.
"""


def hourly_employee_input():
    user_name = input('Please enter a name: ')
    try:
        hours_worked = int(input('Enter the number of hours worked please: '))
    except ValueError as err0r:
        print('\n\nHey jabronie, the input you entered didn\'t match the data type expected.\n')
        raise
    try:
        hourly_wage = float(input('What is the hourly rate of pay? '))
    except ValueError as err0r:
        print('\n\nHey jabronie, the input you entered didn\'t match the data type expected.\n')
        raise

    print('\nEmployee Name:', user_name,
          '\nHours Worked:', hours_worked,
          '\nHourly Wage:', '{:4.2f}'.format(hourly_wage))


if __name__ == '__main__':
    hourly_employee_input()
