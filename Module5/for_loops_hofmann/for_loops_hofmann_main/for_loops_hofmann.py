"""
Program: for_loops_hofmann.py
Author: Nick Hofmann | nickhofmann1989@hotmail.com | nohofmann@dmacc.edu
Last Modified: 6/14/2020

Program specifications: The program will demonstrate some simple for loop
concepts in Python.
"""
numbers = [5.56, 33.987, 99.99999, 13.37, 9.000, 867.5309]
for number in numbers:
    print(number)

print()

for back_from_99 in range(99, 32, -2):
    print(back_from_99)
