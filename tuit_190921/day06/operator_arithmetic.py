# operator arithmetic

a = 9
b = 2

c = a + b
print("{} + {} = {}".format(a, b, c))

c = a - b
print("{} - {} = {}".format(a, b, c))

c = a * b
print("{} * {} = {}".format(a, b, c))

c = a / b
print("{} / {} = {}".format(a, b, c))
print(type(c))

c = 8/2
print("{} / {} = {}".format(8, 2, c))
print(type(c))

c = a % b
print("{} % {} = {}".format(a, b, c))

c = 11 % 4
print("{} % {} = {}".format(11, 4, c))

# 6 % 2 = 0
# 8 % 3 = 2 ,  8/3 = 2....2

c = a // b
print("{} // {} = {}".format(a, b, c))

# round(4.5) => 5
# floor division (4.8) => 4
# floor division (4.9999999999) => 4
# floor division    4   4.5 4.8   5

c = a ** b
print("{} ** {} = {}".format(a, b, c))

c = 3 ** 3
print("{} ** {} = {}".format(3, 3, c))

