"""
quiz_10_q2
"""
# multiplication from 1 to 20
# method 1
lower = 2
upper = 22
step = 2
result = 1
for i in range(lower, upper, step):
    result *= i

print("1*2*4*6*8*...*20 = {}".format(result))

print()
# method 2
lower_2 = 1
upper_2 = 11
result_2 = 1
for i in range(lower_2, upper_2):
    result_2 *= 2*i

print("1*2*4*6*8*...*20 = {}".format(result_2))

