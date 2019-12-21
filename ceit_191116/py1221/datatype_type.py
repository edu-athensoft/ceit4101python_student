"""
datatype
type()
isinstance()
"""

a = "abc"
print(type(a))

a = 1
print(type(a))

print(type("abc"))
print(type(True))
print(type(1.5))
print(type(1))
print(type(None))

print(isinstance(1, int))

# good example
print(isinstance(True, int))
print(isinstance(None, type(None)))

