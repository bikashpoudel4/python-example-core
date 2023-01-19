"""Exercise: Friuit Salad"""

"""
Write a script that will pick 3 fruits from a list of fruits and print the three names of fruits.
Could you make sure that three fruits are different.
"""

import random

fruits = ["Apple", "Banana", "Mango", "Orange", "Peach", "Papaya"]
salad = random.sample(fruits, 3)
print(salad)