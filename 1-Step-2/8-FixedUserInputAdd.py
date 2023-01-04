"""Add numbers entered by the user (FIXED)"""

# fixed of 7-UserInputAddition.py
# we have to parse it to int() after input()
def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    
    # parse
    add = int(a) + int(b)
    
    print("add", add)

main()

"""
In order to convert the string to numbers use functions as:-
    - the int() for integer
    - the float() for floating
as per your situation.
"""