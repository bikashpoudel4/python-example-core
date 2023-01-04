"""Command line arguments - exit"""


import sys
def main():
    if len(sys.argv) != 2:
        exit("Usage : " + sys.argv[0] + " value")
    print("Hello" + sys.argv[1])

main()

"""
To run argv[], we neet to run:
    - python file_name argv
    - python 24-CmdLineArgv-exit.py 12
"""