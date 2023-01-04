"""Command line arguements"""

import sys

# Example 1
# this throws exception as list index out of range.
def main():
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
    
main()

"""
To run program argv.
    - python file_name.py one
"""