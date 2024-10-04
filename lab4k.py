# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 4th, 2024
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab3k.py

# TO DO 1: Add the docstring
# @Function definition: Takes the first letter of each name in the list
# @param: list of names
# @return: list of initials
# TO DO 2: Create the function instructed in readme.md file.
def initials(*args):
    initial_list = []
    for i in args:
        initial_list.append(i[0])
    return initial_list

# TO DO 3: Call the function.
print(initials("Alice","Bob","Charlie","David"))