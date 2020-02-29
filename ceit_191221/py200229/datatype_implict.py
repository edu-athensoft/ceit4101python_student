"""
implicit conversion
"""

# float + int
# float + int -> float
# float + float
# float
a = 1.5 + 1
print(a)

# float + str -> error
# s = 1.5 + 'abc'
s = str(1.5) + 'abc'
print(s)
