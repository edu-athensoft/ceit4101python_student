"""
output formatting
"""

name = "Peter"
password = "12345"

# argument
# argument v.s. parameter
# index
print("Welcome {}! Your password is {}".format(name, password))

# positional arguments
print("Welcome {1}! Your password is {0}".format(name, password))

# keyword arguments
print("Welcome {nm}! Your password is {pwd}".format(nm=name, pwd=password))




