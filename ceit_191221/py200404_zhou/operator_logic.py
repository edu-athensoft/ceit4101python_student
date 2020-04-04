"""
logic operator
"""

# and, or, not

bool1 = (not True) or False
print("bool1 =", bool1)

bool1 = not (True or False)
print("bool1 =", bool1)

# the priority of not comparing with and/or
bool1 = not (True and False)
print("bool1 =", bool1)

bool1 = (not True) and False
print("bool1 =", bool1)

bool1 = not True and False
print("bool1 =", bool1)


print("=====")
bool2 = not (True and False)

