"""Modules"""

# [sys] module which is also known as system module
# below we are importing sys module and printing informations related to sys

import sys

print("1.Output of sys.executable(virtul env/ from where python is running) is: --", sys.executable) 
print("2.Output of sys.platform(OS) is: --", sys.platform) 
print("3.Output of sys.argv(location of file) is: --", sys.argv[0]) 
print("4.Output of sys.version_info.major(version python) is: --", sys.version_info.major) 

print("5.Output of sys.getsizeof(1) is: --", sys.getsizeof(1))
print("6.Output of sys.getsizeof(42) is: --", sys.getsizeof(42))
print("7.Output of sys.getsizeof(1.0) is: --", sys.getsizeof(1.0))

print("8.Output of sys.getsizeof("") is: --", sys.getsizeof(""))
print("9.Output of sys.getsizeof('a') is: --", sys.getsizeof("a"))
print("10.Output of sys.getsizeof('ab') is: --", sys.getsizeof("ab"))
print("11.Output of sys.getsizeof('abcdefghijk') is: --", sys.getsizeof("abcdefghijk"))

