"""
dataype convertion
"""

str1 = "123"
print(str1, type(str1))

num1 = int(123)
print(num1, type(num1))

# do not use int() like this:
# num1 = int("1.23")
# print(num1, type(num1))

#
# num1 = int("abc")
# print(num1, type(num1))



# string -> float
str1 = "12.3"
print(str1, type(str1))

num1 = float(str1)
print(num1, type(num1))


# str()     V
# string()  X

float1 = 1.23
print(float1, type(float1))

str1 = str(float1)
print(str1, type(str1))


# int -> float
print(float(100))


# float -> int
print(int(100.999))
