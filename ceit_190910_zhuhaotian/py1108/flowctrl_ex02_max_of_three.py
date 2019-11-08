#
a = 3
b = 9
c = 6

max = a

if a > b and a > c:
    max = a

if a > b and a < c:
    max = c

if a < b and a < c:
    if b < c:
        max = c
    else:
        max = b

if a < b and a > c:
    max = b


print("solution1: max is {}".format(max))
print()


# case 2
if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c
print("solution2: max is {}".format(max))