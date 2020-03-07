"""
datatype conversion : implicit conversion
"""

result = 1.5 + 1
print(result, type(result))

# float + int
# +
# 1.5 -> float
# 1 -> int -> float (automatically converted)

# result = 1.5 + 'abc'
# print(result, type(result))

# result = 1.5 + '1.23'
# print(result, type(result))

# explicit type conversion
result = 1.5 + float("1.23")
print(result, type(result))