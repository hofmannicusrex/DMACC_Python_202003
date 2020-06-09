"""
Program: basic_if_elif_statements_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/8/2020

Program specifications: The program will return the cost of the membership
to the Programmer's Toolkit Monthly Subscription Box.
"""

print('Welcome to the registration location for the \'Programmer\'s Toolkit Monthly Subscription Box!\'')
print('Please choose one of these membership tiers (case-sensitive):\n')
user_input = input('"Platinum", "Gold", "Silver", "Bronze", "Free Trial": ')

if user_input == 'Platinum':
    print()
    print('Whoa high roller,', user_input, 'membership costs $60 a month.')
elif user_input == 'Gold':
    print()
    print(user_input, 'membership costs $50 a month.')
elif user_input == 'Silver':
    print()
    print(user_input, 'membership costs $40 a month.')
elif user_input == 'Bronze':
    print()
    print(user_input, 'membership costs $30 a month.')
elif user_input == 'Free Trial':
    print()
    print('You\'re in luck! The', user_input, 'costs nothing!!!')
