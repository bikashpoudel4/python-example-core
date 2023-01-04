"""The main function called"""

# INFO ==
"""
You could write your code in the main body of your python file, but using functions and passing arguements to it will make your code easier
to maintain and understand. Therefore I recommend that you always write every script with a function called "main".

    - Function defination starts with the def keyword,followed by the name of the new function,
        ("main" in this case), followed by the list of parameters in parentheses(nothing in this case as in example)
    
    - The content or body of the function is then indented to the right,
    
    - The function definition ends when the indentation stops.
    
    - The content or the body of the function is then indented to the right.
    
    - The function defination ends when the indentation stops.
"""

# Example
def main():
    print("Hello")
    print("You!")

print("before")
main()
print("after")

"""
In above example program main function,
    - the function's body which is [HELLO and YOU!] are executed [BEFORE]
        -- calculations and computations is done inside indentend function's body [Hello and You!]
        -- result can be executed after block is ended [Before]
        -- 
    
    - example of this function can be found in next 3-ExMFC.py file
"""