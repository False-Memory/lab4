# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 4th, 2024
# Purpose: Create the complete calculator function using keyword parameters.
# Usage: ./lab3j.py

# TO DO 1: Add the docstring
# @Function definition:  calculates the 2 numbers based on the operation given
# @param: Takes in 3 parameters, 2 number and one operation
# @return: returns the result of the 2 numbers that has gone through the operation
# TO DO 2: Copy the code from lab4i.py.
def compute(num1, num2, symb='+'):
    if symb == '+':
        return num1 + num2
    elif symb == '-':
        return num1 - num2
    elif symb == '*':
        return num1 * num2
    else:
        return num1 / num2

#Create the main functions.
def main():
    num1 = input("Enter a number: ")
    while num1.isdigit() == False:
        num1 = input("Please enter a valid number: ")
    num2 = input("Enter another number: ")
    while num2.isdigit() == False:
        num2 = input("Please enter a valid integer: ")
    num1, num2 = int(num1),int(num2)
    oper = input("Enter the operation you would like to perform(+,-,*,/): ")

    while oper != "+" and oper != "-" and oper != "*" and oper != "/":
        oper = input("Please enter one of the following symbols(+,-,*,/): ")

# TO DO 3: Modify the parameters to behave as keyword parameters.
    print(compute(num1 = num1 ,num2 = num2 ,symb = oper))


#Call the compute function.
print(compute(num1 = 13,num2 = 45,symb ='*'))
print(compute(num1 = 13,num2 = 45,symb ='/'))
print(compute(num1 = 13,num2 = 45,symb ='-'))
print(compute(num1 = 13,num2 = 45,symb ='+'))
print(compute(num1 = 13,num2 = 45))
#Call main function
main()


