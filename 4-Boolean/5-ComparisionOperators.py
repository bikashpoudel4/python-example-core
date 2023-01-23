"""Comparision Operators"""

"""
==  equal
!=  not equal

<   less than
<=  less than or equal
>   greater than
>=  greater than or equal
"""

# Example
a = "42"
b = 42

print(a == b) # False
print(a != b) # True
print (b == 42.0) #True

print(None == None) # True
print(None == False) # False

# DO NOT COMPARE DIFFERENT TYPES

x = 24
y = 9
print(x > y) # True

c = "19"
d = "9"
print(c > d) # False

e = "55"
f = 24
print(x > y) # True

g = 33
h = "2"
print(g > h) # False 