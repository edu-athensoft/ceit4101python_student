"""
Number formatting with padding for int and floats
"""

# case 1
print("{:5d}".format(12))

# case 2
print("{:2d}".format(1234))

# case 3
print("{:8.3f}".format(12.2346))

# case 4
print("{:05d}".format(12))