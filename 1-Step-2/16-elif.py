"""Conditionals: elif """

# Example
def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    
    if a == b:
        print("They are equal.")
    elif int(a) < int(b):
        print(a + " is less than(<) " + b)
    else:
        print(a + " is greater than (>) " + b)

main()