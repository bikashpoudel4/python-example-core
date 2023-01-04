"""Adding numbers entered by the user (OUPS = mistake)"""

# here input of a and b are in string, while adding with + its concatenates a and b 
def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    add = a + b
    print(add)

main()

"""
When reading from the command line using input(),
    - the resulting value is a string.
    - Even if you add only typed in digits, therefore 
        --the addition operator + concatenates the string
"""