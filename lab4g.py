# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian 
# Date: October 4th, 2024
# Purpose: Create Some Complex Functions.
# Usage: ./lab3g.py

# TO DO 1: Add the docstring
# @Function definition: This function saves all even numbers from a list of numbers onto a seperate list and returns that list
# @param: a list of integers
# @return: a list of even integers
# TO DO 2: Create the function.
def show_even(*args):
    even = []
    for i in args:
        if i % 2 == 0:
            even.append(i)
    return even

# TO DO 3: Call the function.
print(show_even(1,2,3,4,5,6,7,8))
print(show_even(1,3,5,7,9,11,13,15,17))