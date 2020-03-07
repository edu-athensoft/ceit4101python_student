"""
data type of literal and variables/constants
"""

# type()
# built-in function
num = 999
print(num, type(num))

print(num, type(999))

str1 = "hello world"
print(str1, type(str1))
print(str1, type("hello world"))

# isinstance()
bool1 = False
print(isinstance(bool1, bool))
