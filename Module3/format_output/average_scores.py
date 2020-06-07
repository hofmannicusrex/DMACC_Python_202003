"""
Program: average_scores.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/6/2020

Program specifications: The program will.
"""

# METHODS


def average():
    # Get input for scores
    test_score_1 = input('Please enter the test score: ')
    test_score_2 = input('Please enter the test score: ')
    test_score_3 = input('Please enter the test score: ')

    # return calculate_average(test_score_1, test_score_2, test_score_3)  # Alternative way return statement.
    return (test_score_1 + test_score_2 + test_score_3) / 3  # calculation using score1, score2 and score3

# Alternative way presented by the professor.
# I wrote out this code because it was a great refresher for me as I took last semester off and I'm
# not a coding expert yet.


def calculate_average(score1, score2, score3):
    score_average = ((score1 + score2 + score3) / 3)  # I'm a fan of parentheses.
    return score_average
