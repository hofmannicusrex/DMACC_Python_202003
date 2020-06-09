"""
Program: if_elif_main.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/8/2020

Program specifications: The program will return the cost of the membership
to the Programmer's Toolkit Monthly Subscription Box.
"""


def membership_lvl_prompt():  # Method to prompt the user for their membership tier choice.
    print('Welcome to the registration location for the \'Programmer\'s Toolkit Monthly Subscription Box!\'')
    print('Please choose one of these membership tiers (case-sensitive):\n')
    user_membership_input = input('"Platinum", "Gold", "Silver", "Bronze", "Free Trial": ')

    return user_membership_input


def determine_membership_lvl(user_input):  # Method to determine the cost of the user's membership tier.
    # It accepts one parameter
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

    return user_input  # Make sure to return the value of 'user_input', which is going to be a string in this case.


if __name__ == '__main__':
    # Assigning the value returned from the method 'membership_lvl_prompt' to 'user_entry'
    user_entry = membership_lvl_prompt()
    # Calling the 'determine_membership_lvl' and passing it the value of 'user_entry'
    determine_membership_lvl(user_entry)
