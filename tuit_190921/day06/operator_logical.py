# logical operators

# and
a = True
b = True
result = a and b
print("{} and {} is {}".format(a, b, result))

a = True
b = False
result = a and b
print("{} and {} is {}".format(a, b, result))

a = False
b = True
result = a and b
print("{} and {} is {}".format(a, b, result))

a = False
b = False
result = a and b
print("{} and {} is {}".format(a, b, result))

print()

# or
a = True
b = True
result = a or b
print("{} or {} is {}".format(a, b, result))

a = True
b = False
result = a or b
print("{} or {} is {}".format(a, b, result))

a = False
b = True
result = a or b
print("{} or {} is {}".format(a, b, result))

a = False
b = False
result = a or b
print("{} or {} is {}".format(a, b, result))

print()

# not
a = True
result = not a
print("not {} is {} ".format(a, result))

a = False
result = not a
print("not {} is {} ".format(a, result))