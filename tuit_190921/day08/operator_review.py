# divide operator
a = 1
b = 2
result = a / b
print("result of {}/{} is {}".format(a, b, result))
print("the type of result is", type(result))

# modulus operator
a = 5
b = 2
result = a % b
print("result of {}%{} is {}".format(a, b, result))

# floor division
a = 5
b = 2
result = a // b
print("result of {}//{} is {}".format(a, b, result))
#  2.5
#  1,  2,  2.5,  3,  5

# exponent
a = 5
b = 10000
result = a ** b
print("result of {}**{} is {}".format(a, b, result))

# equal to
a = 5
b = 3
result = a == b
print("result of a==b is {}".format(result))

# not equal to
a = 5
b = 3
result = a != b
print("result of a!=b is {}".format(result))

# logical operator
a = True
b = False
result = a and b
print("result of {} and {} is {}".format(a, b, result))

result = a or b
print("result of {} or {} is {}".format(a, b, result))

result = not a
print("result of not {} is {}".format(a, result))

# assignment operator
a = 5
a += 3
print("a is {}".format(a))
# a += 3 => a = a + 3

a = 5
a -= 3
print("a is {}".format(a))
# a -= 3 => a = a - 3

a = 5
a *= 3
print("a is {}".format(a))
# a *= 3 => a = a * 3

a = 5
a /= 3
print("a is {}".format(a))
# a /= 3 => a = a / 3


# identity operator
x = 5
y = 5
result = x is y
print("{} is {} ? the result is {}".format(x,y, result))

x = "abc"
y = "abc"
result = x is y
print("{} is {} ? the result is {}".format(x,y, result))

x = 5
y = 5
result = x is not y
print("{} is not {} ? the result is {}".format(x,y, result))

x = "abc"
y = "abc"
result = x is not y
print("{} is not {} ? the result is {}".format(x,y, result))


# membership operator
str = "hello world"
result = 'h' in str
print("h in {} ?  {}".format(str, result))

result = 'z' in str
print("z in {} ?  {}".format(str, result))

result = 'h' not in str
print("h not in {} ?  {}".format(str, result))

result = 'z' not in str
print("z not in {} ?  {}".format(str, result))
