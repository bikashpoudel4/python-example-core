"""Exercise : Rectangular"""

# Question
"""
- Write a script that will ask for the sides of a rectangular and print out the area.
- Provide error messages if either of the sides is negative or 0.
    -- side : 5
    -- side : 10
    -- The area of rectangle is 12.
    
    **** Formula area = length * width
"""

def main():
    # parsing string into int
    length = int(input("Enter Length : "))
    width = int(input("Enter Width : "))
    
    if length <= 0:
        print("Length is not positive or 0.")
        return
    
    if width <= 0:
        print("Width is not positive or 0.")
        return
    
    # area of rectangle formula
    area = length * width
    print("The area is ", area)
    
main()