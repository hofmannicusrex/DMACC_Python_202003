"""
Program: basic_list.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/20/2020

Program specifications: This program will .
"""


# range(beginning value, ending value, increment/decrement amount)
# This counts backwards from 50 to 0 (5)
# for loop_counter in range(50, 0, -5):
#        print(loop_counter)

# range(beginning value, ending value, increment/decrement amount)
# This counts up from 0 to 50 (45)
# for loop_counter in range(0, 50, 5):
#        print(loop_counter)


def get_input():
    """
    :param parameter_1:
    :param parameter_2:
    :return: Return a string
    :raises keyError: raises an exception
    """

    # ask for user input ONE TIME I believe
    # return a string of that user input
    user_input = input('Please enter a number:')

    return user_input


def make_list():
    """
    :return: Returns a list.
    :raises keyError: raises an exception
    """
    user_created_list = []
    for loop_iteration in range(3):
        # TRY and cast to a numeric type. I'm guessing that they'll want the user to re-enter their input if it can't be casted
        # RAISE an exception if it can't convert
        # APPEND it to our list declared up above

        try:
            input_from_user = int(get_input())
        except ValueError as input_error:
            # raise input_error
            # while input_error is ValueError:  # This doesn't work either
            print('That is not correct input. Please enter a number.')
            input_from_user = int(get_input())

        user_created_list.append(input_from_user)

        # How the hell are you supposed to add something using index? Instructions say that is the best
        # way for the next assignment. All it does is look for an item that can't possibly be in the list yet.
        # Always going to error out.
        # user_created_list.index(input_from_user, loop_iteration)

    # return our list up above
    return user_created_list


if __name__ == '__main__':
    print(make_list())
