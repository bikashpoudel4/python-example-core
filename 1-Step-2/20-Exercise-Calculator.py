"""Exercise : Calculator"""

# question

"""
Create a script that accepts 2 numbers and an operator (+, -, *, /), and prints the result of the operation.
"""

def main():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    operator = input("Select Operator(+ - * /): ")
    
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        print("Invalid Operator: '{}'".format(operator))
        return
    print(result)
    return

main()