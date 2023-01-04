"""Convert string to int"""

# taking 43 as string and 
# checking its type
a = "47"
print(a)
print("data type of a", type(a))

# saving variable a's value in variable b and
# converting value into int by parsing using int() function
b = int(a)
print("value of b: ", b)
print("data type of b", type(b))

# example that cannot be done
c = "20 is a number"
print("data type of c is: ", type(c))

d = int(c)
print("data type of d is: ", type(d))