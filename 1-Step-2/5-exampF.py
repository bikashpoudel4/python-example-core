
"""
* write 
    - takes exactly one parameter
"""
import sys

sys.stdout.write("Hello")
sys.stdout.write("You!")
# =====================================

"""
* end
    - will set the character added at the end of each print statement.
"""
print("2Hello", end=" ")
print("2You!")
# ==========================

"""
* sep
    - wii ste the character separating values.
"""
print("3Hello", "3You!", sep="")
print("4Hello", "4You!", sep="     ")