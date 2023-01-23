"""Exercise: Compare Numbers"""

# QUESTION
"""
Q.  Ask the user to enter two numbers and tell us which one is bigger. 
"""
# # Parsing in to integer from strings.
# num_one = int(input("Please type in a string: "))
# num_two = int(input("Please type in another string: "))

# STRING form
num_one = input("Please type first number: ")
num_two = input("Please type second number: ")
print("How to compare: ")
print(" 1. ASCII")
print(" 2. Length")
how = input()

if how == '1':
    first = num_one > num_two
    second = num_one < num_two
elif how == '2':
    first = len(num_one) > len(num_two)
    second = len(num_one) < len(num_two)

if first:
    print("First number is bigger.")
elif second:
    print("Second number is bigger.")
else:
    print("They are equal.")