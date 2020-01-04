"""
datatype
convert
"""

# print("abc"+123)  # error occurs

# str -> int
# print(int("123bc"))

# decimal -> binary
print(bin(10))

# int -> str
print("abc"+str(123))

# implicit type conversion
print(1.5 + 0.3)
print(1.5 + 3)   # implicit type conversion
# 1.5 + float(3)  if compatible

# explicit type conversion
# print(1.5 + "3")
# float + str
print(str(1.5)+"3")
print(1.5+float(3))

