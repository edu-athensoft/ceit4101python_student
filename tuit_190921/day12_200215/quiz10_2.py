"""
quiz 10-2
to calculate the sequence of number
"""

"""
1X2X4x6.......X20

(2x1) (2x2) (2x3) (2x4) ... (2x10)
"""

# print(list(range(1,11)))

product = 1
for i in range(1,11):
    # print(2*i, end=",")
    product *= 2*i
print()

print("The product of 1x2x4x6.....x20 is: {} ".format(product))





