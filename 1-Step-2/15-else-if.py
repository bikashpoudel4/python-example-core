"""Conditionals: else if """

def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    
    if a == b:
        print("The both numbers are equal.")
    else:
        if int(a) < int(b):
            print(a + " is less than (<)" + b)
        else:
            print(a + " is greater than (>) " + b)
            
main()