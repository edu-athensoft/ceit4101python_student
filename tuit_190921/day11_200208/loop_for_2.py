"""
for loop
summary
1,2,3,4,....,100
"""

"""
sum = 0

1 + sum -> sum = 1
2 + sum -> sum = 3
3 + sum -> sum = 6

i + sum -> sum

100 + sum -> sum = ?
"""

sum = 0
for i in range(1,1001):
    sum = sum + i

print("The result is {}".format(sum))





