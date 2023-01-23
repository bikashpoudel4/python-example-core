"""Exercise: Compare Strings"""

# QUESTION and HINTS
"""
Q.  Compare Strings
H.      - Ask the user to entner two strings.
        - Then ask the user to select if she wants to compare them based on ASCII or based on their length.
        - Then tell us which one is bigger.
"""

# Steps to follow
"""
    - Input a string: (user types string and ENTER)
    - In another String: (user types string and ENTER)
    - 1.ASCII
    - 2.Length
    (User types 1 or 2 and Enter)
"""
# Solution
first_str = input("Please type in a string: ")
second_str = input("Please type in second String: ")
print("How to compare? : ")
print(" 1. ASCII")
print(" 2. Length")
how = input()

if how == "1":
    first = first_str > second_str
    second = first_str < second_str
elif how == "2":
    first = len(first_str) > len(second_str)
    second = len(first_str) < len(second_str)

if first:
    print("First string is bigger than second string.")
elif second:
    print("Second string is bigger than first string.")
else:
    print("The both strings are equal")