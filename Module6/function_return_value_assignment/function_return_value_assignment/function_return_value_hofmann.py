"""
Program: function_return_value_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/15/2020

Program specifications: The program will demonstrate a simple method call with a return
value. It will handle simple input errors using a try-catch statement as well.
"""


def hourly_employee_input():
    """ This prompts the user for input that will get used in the weekly_pay function
    and the main method.
    """
    user_name = input('Please enter a name: ')
    try:
        hours_worked = int(input('Enter the number of hours worked in one day please: '))
    except ValueError as err0r:
        print('\n\nHey jabronie, the input you entered didn\'t match the data type expected.\n')
        raise
    try:
        hourly_wage = float(input('What is the hourly rate of pay? '))
    except ValueError as err0r:
        print('\n\nHey jabronie, the input you entered didn\'t match the data type expected.\n')
        raise

    print("\nEmployee Name: " + user_name + "\nWeekly Pay: $" + str(weekly_pay(hours_worked, hourly_wage)))


def weekly_pay(hours_worked, hourly_pay_rate):
    """ This calculates the weekly pay by multiplying the daily number by 5
    :param hours_worked: the number of hours that the user enters
    :param hourly_pay_rate: the hourly rate of pay that the use enters
    :returns the weekly pay based off of the daily rate * 5
    """
    calculated_weekly_pay = (hours_worked * hourly_pay_rate) * 5
    return '{:6.2f}'.format(calculated_weekly_pay)


if __name__ == '__main__':
    try:
        print_summary = hourly_employee_input()
    except ValueError as error:
        print('\n\nHey jabronie, the input you entered didn\'t match the data type expected.\n')
        raise
    else:
        print_summary  # Not sure if this was the equivalent of what that example showed.
