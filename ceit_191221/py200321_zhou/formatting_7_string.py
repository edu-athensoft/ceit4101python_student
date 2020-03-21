"""
String formatting with padding and alignment

<	Left aligned to the remaining space
^	Center aligned to the remaining space
>	Right aligned to the remaining space
=	Forces the signed (+) (-) to the leftmost position
"""


# string padding with left alignment
print("|{:5}|".format("cat"))

# string padding with right alignment
print("|{:>5}|".format("cat"))

# string padding with center alignment
print("|{:^5}|".format("cat"))

# string padding with center alignment
# and '*' padding character
print("|{:*^5}|".format("cat"))
print("|{:?^7}|".format("cat"))
print("|{:=^9}|".format("cat"))
