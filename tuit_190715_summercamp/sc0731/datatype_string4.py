
a = 15
b = 12
c = "abc"

str1 = "Binary representation of {0} , {1} , {2} ".format(a,b, c)
print(str1)

n1 = 15
n2 = 12
n3 = 8
str2 = "Binary representation of {0} {0} {0} is {0:x},  {1} is {1:x}, {2} is {2:x}".format(n1, n2, n3)
print(str2)

str3 = "Exponent representation: {0:e}".format(1566.345)
print(str3)

str4 = "One third is: {0:.3f}".format(1/3)
print(str4)
# 0.33333333333333333333
# 0.333