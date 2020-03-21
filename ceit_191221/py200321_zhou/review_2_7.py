"""
review input, output and import
"""

import sys as sy

# input - built-in function
# echo
print(input("Enter you name:"))
# print(input("Enter you name:"), type())       # not recommended

# using a variable
name = input("Enter you name:")
print('type of {} is {}'.format(name, type(name)))

# output, formatting
# by default
name = 'Athens'
print('type of {} is {}'.format(name, type(name)))

# positional arg
print('type of {0} is {1}'.format(name, type(name)))
print('type of {1} is {0}'.format(name, type(name)))

# keywords arg
print('type of {nm} is {nmtype}'.format(nm = name, nmtype = type(name)))

print(sy.api_version)
print(sy.path)