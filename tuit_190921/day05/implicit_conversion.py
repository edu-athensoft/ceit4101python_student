# type conversion
# implicit conversion

# example 1
num_int = 123
num_float = 12.3

result = num_int + num_float
print(result, type(result))

# example 2
num_int = 456
num_str = 'abc'

result = str(num_int) + num_str
print(result, type(result))