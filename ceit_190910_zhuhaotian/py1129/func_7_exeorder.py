# input x, return x**3, output results
# 10 times

# loop
# call for 10 times

import random


def cube(x):
    return x**3

# my_num = [1,4,3,5,32,6,7]
for i in range(0, 6):
    x = random.randint(1,6)
    print(cube(x))


