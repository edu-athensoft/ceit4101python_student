
# prod = 1
# for i in range(1,7):
#     prod *= i
#
# print(prod)


# 6! = 6*5*4*3*2*1
# 6! = 6 * 5!
# 6! = 6 * 5 * 4!
# ...
# 6! = 6 * 5 * 4 * 3 * 2 * 1!

# set 1! = 1

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(6))
