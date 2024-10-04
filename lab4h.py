# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian 
# Date: October 4th, 2024
# Purpose: Create the main Function.
# Usage: ./lab3h.py

# TO DO 1: Add the docstring
# @Function definition: Takes in 2 numbers and returns the sum of these two numbers
# @param: 2 integer numbers
# @return: the sum of the 2 integer numbers
# TO DO 2: Create the function sum.
def sum(num1, num2):
    return num1+num2

# TO DO 3: Create the main functions.
def main():
# TO DO 4: Call the sum function.
    num1 = input("Enter a number: ")
    
    while num1.isdigit() == False:
        num1 = input("Please enter a valid integer: ")
    num2 = input("Enter another number: ")
    
    while num2.isdigit() == False:
        num2 = input("Please enter a valid integer: ")

    num1,num2 = int(num1), int(num2)

    print("The sum of",num1,"and",num2,"is",sum(num1,num2))
# TO DO 5: Call the main function.
main()