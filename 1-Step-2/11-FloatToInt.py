"""Converting float to int"""

a = 3.1
print("data type of a is: ", type(a))
print(a)

b = int(3.1)
print("data type of b is: ", type(b))
print(b)


# # We cannot do this 
# # below example throws error
# # UNCOMMENT TO SEE THE RESULT

# c = "5.5"
# print("data type of c is: ", type(c))
# print(c)

# d = int(c)
# print("data type of d is: ", type(d))
# print(d)

"""Conversion of float string to int"""
# STEPS
"""
1. first variable e has string which consists of floating value
2. converting e=string into float value, and saving in f=float value
3. conversion of float value f to int, saving it to g=int value
"""
e = "8.7" # str
f = float(e)
g = int(f)

print(g)
# checking types
print("data type of e is: ", type(e))
print("data type of f is: ", type(f))
print("data type of g is: ", type(g))

# conversion
h = int(float(e))
print(h)
print(type(h))

print(int(float(9.1)))
print(int(float("9")))
print(int(float(9)))


