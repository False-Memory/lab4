# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 4th, 2024
# Purpose: Create Simple Functions.
# Usage: ./lab3f.py


# TO DO 1: Add the docstring
# TO DO 2: Create the function.
# @Function definition: The function will return true if a list contains an even number
# @param: a list
# @return: True/False 
def has_even(*args):
    for i in args:
        if i % 2 == 0:
            return True
    return False
        
# TO DO 3: Call the function.
if has_even(1,2,3,1,5,1) == True:
    print("The list contains an even number")
else:
    print("The list does not contain an even number")