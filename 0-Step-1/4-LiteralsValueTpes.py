"""Literals, Value Types in Python"""

print(type(23)) # int
print(type(9.24)) # float
print(type("hello")) # Str

print(type("65")) # Str
print(type("6.91")) # Str

print(type(None)) # NoneType
print(type(True)) # bool
print(type(False)) # bool

print(type([])) # List
print(type({})) # Dict

print(type(hello)) # NameError: name 'hello is not defined'
print("Still running")

# Floating point Limitation
print(0.1 + 0.2) # 0.30000000000000004