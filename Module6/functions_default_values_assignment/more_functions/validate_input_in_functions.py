"""
Program: validate_input_in_functions.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/17/2020

Program specifications: This program will repeatedly ask the user .
"""

"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


if __name__ == '__main__':
    ask_ok('Do you really want to quit?')
"""

"""     MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE
def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    while True:
        test_score_entry = int(input(test_name))
        if 0 <= test_score_entry <= 100:
            test_score_string = 'Test name: ' + str(test_score_entry)
            print(test_score_string)
            return
        print('You entered:', test_score_entry, '\nThat is not in range: please try again. :)\n')
        MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE MY CODE """


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: The name of the test...not really sure what a "test name" is but the
                      assignment requires it.
    :param test_score: The score that was earned on the test.
    :param invalid_message: The message that will be displayed upon the user entering a bad
                            input.
    :return: Returns valid input in this format: "test_name: test_score"
    """
    # return {test_name: test_score}
    return
    pass


if __name__ == '__main__':
    # score_input('Please enter a test score between 0 and 100, please and spank you: ')
    user_test_name = input('Please enter your name: ')
    user_test_score = input('Please enter a test score between 0 and 100, please and spank you: ')
    # int-casting user_test_score might not be necessary.
    score_input(user_test_name, int(user_test_score))  # Consider wrapping this in a print statement.
