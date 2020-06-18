"""
Program: validate_input_in_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/17/2020

Program specifications: This program will repeatedly ask the user for a valid test
score until it is range (0-100). It will then display the test taker's name and score.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again! '):
    """
    :param test_name: The name of the test taker.
    :param test_score: The score that was earned on the test.
    :param invalid_message: The message that will be displayed upon the user entering bad input.
    :return: Returns valid input in this format: "test_name: test_score"
    """

    while True:

        if test_score < 0 or test_score > 100:
            test_score = int(input(invalid_message))

        else:
            final_output = '\n' + test_name + ': ' + str(test_score) + '%'
            return final_output
    pass


if __name__ == '__main__':
    user_test_name = input('Please enter your name: ')
    user_test_score = int(input('Please enter a test score between 0 and 100, please and spank you: '))
    print(score_input(user_test_name, user_test_score))
