# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 4th, 2024
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab3l.py

# TO DO 1: Create Variable Numbers.
numbers = [2,3,4,5,6,7,8,9,10]

result = map(lambda num: num**2, numbers)
square = list(result)
# TO DO 2: Print squared values of Numbers.
print(square)

# TO DO 3: Print variable Divisibleby2.
result = filter(lambda x: x%2 == 0, numbers)
divisibleby2 = list(result)
print(divisibleby2)