""" Exercise : Calculator argv """

"""
Create a script that accepts 2 numbers and an operator (+. -. *. /), on the command line and prints the result of the operation.

"""
import sys

def main():
    if len(sys.argv) < 4:
        exit("Usage : " + sys.argv[0] + "OPERAND OPERATOR OPERAND")
        
    a = float(sys.argv[1])
    b = float (sys.argv[3])
    operator = sys.argv[2]
    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        print("Invalid Operator: '{}'".format(operator))
        exit()
    print(result)
main()