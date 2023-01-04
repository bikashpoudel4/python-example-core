"""
How can we check that
    -   if a string can be converted to a number ?
"""

# sol

value = input("Enter a number: ")
print(value)

print(value.isdecimal())
print(value.isnumeric())

if value.isdecimal():
    num = int(value)
    print(num)
    
"""
- We will talk about this later. For now assume that the user enters something
    that cannot be converted to a number.

- Use Regular Expressions (regexes) to verify that the input string looks like a number.

- Wrap the code in try-except block to catch any exception raised during the conversion. 
"""