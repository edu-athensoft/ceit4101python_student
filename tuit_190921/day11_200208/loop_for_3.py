"""
print out a multiplication table
12X1 ... 12X12

12x1 = 12
12x2 = 24
12x3 = 36
...
12x12 = 144

using for-loop and string format
"""

A = 9

for i in range(1, A+1):
    print("{} x {} = {}".format(A, i, A*i))

