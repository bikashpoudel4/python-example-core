"""Exercise : Number guessing game - level 0"""

# Question and hints
"""
Level 0.
    - Using the random module the computer "thinks" about a whole number between 1 and 20.
    - The user has to guess the number. After the user types in the guess the computer tells if this was
        bigger or smalle than the number it generated, or if was the same.
    - The game ends after just one guess.

Level 1.
    - Other levels in the next steps
""" 

# Solution
import random

hidden = random.randrange(1, 21)
print("The hidden values is: ", hidden)

user_input = input("Please enter your guess: ")
print(user_input)

guess = int(user_input)
if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is to high.")