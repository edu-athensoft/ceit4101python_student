"""
datatype convertion
"""

# int()
number = int("234")
print("234",type("234"))
print(number,type(number))

# incompatible literal
# number = int("1.23")
# print(number)

# float()
fnum = float("1.60")
print(fnum,type(fnum))

# float -> int
inum = int(fnum)
print(inum , type(inum))

# int -> float
fnum2 = float(inum)
print(fnum2, type(fnum2))

# number -> string
# str()
fnum = 1.23
s1 = str(fnum)
print(s1)

bool1 = True
s2 = str(bool1)
print(s2)



