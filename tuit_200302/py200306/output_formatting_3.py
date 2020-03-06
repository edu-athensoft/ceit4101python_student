"""
try out all the number formatting type
"""

# case - d
print("Hello {0}, your balance is {1:9d}".format("Adam", 230))

# case - c


print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))
print("{:5d}".format(12))

