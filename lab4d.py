# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: October 4th, 2024
# Purpose: Practice slicing on lists.
# Usage: ./lab3d.py

# TO DO 1: Create variable words.
words = []

# TO DO 2: Write a while loop.

while True:
    add_word = input("Enter words(Enter q to quit): ")
    if add_word.lower() == "q":
        break
    else:
        words.append(add_word)

# TO DO 3: Print number of elements in the list.
print(len(words))
# TO DO 4: Create variable someWords.
someWords = []
# TO DO 5: Update someWords.
if len(words) >= 3:
    for i in range(0,3):
        someWords.append(words[i])
if words == someWords:
    print("The 2 lists are equal")
# TO DO 6: Print variable Words.
print(words)
# TO DO 7: Print variable someWords.
print(someWords)