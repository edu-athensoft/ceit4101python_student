# explicit conversion

num_int = 123
num_str = '456'

result = num_int + int(num_str)
print(result, type(result))


# int(), str(), float()


# to test loss of data when doing explicit conversion
num_float = 12.345
a = int(num_float)
print(a)


