"""Exercise : Rectangular(argv)"""

# Question

""" 
Find the area of rectangular, where
    - it will accept the arguments on the command
"""

import sys
def main():
    if len(sys.argv) != 3:
        exit("Needs 2 arguments:  width length")
    
    width = int(sys.argv[1])
    length = int(sys.argv[2])
    
    if length <= 0:
        exit("length is not positive or 0 ")
        
    if width <= 0:
        exit("Width is not positive or 0 ")
    
    area = length * width
    print("The area is ", area)

main()