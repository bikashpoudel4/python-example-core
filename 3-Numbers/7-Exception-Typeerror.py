"""Exception : TypeError: 'module' object is not callable"""

# A common mistake, Calling the class and not calling the method


# ERROR
import random

print("Bikash")
x = random()
print(x)

# ERROR FIXING
import random
x = random.random()
print(x)

# -- OR
from random import random
x = random()
print(x)
