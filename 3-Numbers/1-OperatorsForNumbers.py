"""Operators For Numbers"""

a = 5
b = 2
c = 5.2

d = a + b
print("1.D", d)

print("2.a + b - addition - ", a + b)
print("3.a + c - addition with decimal number - ", a + c)
print("4.b / a - division- ", b / a) # see the __future__
print("5.b // a - floor division - ", b // a)
print("6.a * c - multiplicition -", a * c)

print("7.a ** b - power - 5*5 -", a ** b)

print("8.100 % 50 - modulus - percent -", 17 % 3)

a += 2 # is the same as a = a + 2
print("9.a += 2 -is the same as a = a + 2 - ", a)

# errors
# a++ # SyntaxError : invalid syntax
# a-- # SyntaxError : invalid syntax

a += 1
print("10.a += 1", a)

a -= 1
print("11. a -= 1", a)

"""
There is no auto-increment (++) and auto decrement(-) in python
    - because they can be expressed by += 1 and -= 1 respectively
"""