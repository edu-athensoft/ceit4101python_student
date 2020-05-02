"""
recursion and recursive function
"""

# 1+2+3+4+.....+100

"""
1       s(1)    = 1
1+2     s(2)    = s(1)+2
1+2+3   s(3)    = s(2)+3
1+2+3+4 s(4)    = s(3)+4
...
1+2+3+4+......+n    s(n)

s(n) = s(n-1) + n

"""


def s(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n>1:
        return s(n-1)+n
    else:
        print("Error")

print(s(0))





