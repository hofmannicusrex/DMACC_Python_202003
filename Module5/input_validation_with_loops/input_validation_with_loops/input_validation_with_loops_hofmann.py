"""
Program: input_validation_with_loops_hofmann.py
Author: Nick Hofmann
nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/14/2020

Program specifications: The program will .
"""
# VARIABLE DECLARATIONS
user_list = []
user_number_input = 0
NUMBER_ONE_CONSTANT = 1
NUMBER_100_CONSTANT = 100

while user_number_input != -999:
    # print('\n   inside outer while loop   \n')
    user_number_input = int(input('Please enter a number between 1 and 100. Type (-999) to quit: '))
    user_list.append(user_number_input)

    if user_number_input == -999:
        user_list.remove(-999)
        break

    while user_number_input < NUMBER_ONE_CONSTANT or user_number_input > NUMBER_100_CONSTANT:
        # print('\n   inside inner while loop   \n')
        user_list.pop()
        print('Sorry but that number is not between 1 and 100.')
        user_number_input = int(input('Please enter a number between 1 and 100. Type (-999) to quit: '))
        user_list.append(user_number_input)

        if user_number_input != -999:
            user_list.remove(-999)
            break

# print the list using a for loop
for user_lis in user_list:
    print(user_lis)
