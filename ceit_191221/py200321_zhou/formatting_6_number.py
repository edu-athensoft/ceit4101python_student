"""
Number formatting with alignment

Number formatting with alignment
Type	Meaning
<	Left aligned to the remaining space
^	Center aligned to the remaining space
>	Right aligned to the remaining space
=	Forces the signed (+) (-) to the leftmost position
"""

# integer numbers with right alignment
print("|{:5d}|".format(12))

# float numbers with center alignment
print("|{:^10.3f}|".format(12.2346))

# integer left alignment filled with zeros
print("|{:<05d}|".format(12))
print("|{:05d}|".format(12))

# float numbers with center alignment
print("|{:=10.3f}|".format(-12.2346))
print("|{:=+10.3f}|".format(12.2346))