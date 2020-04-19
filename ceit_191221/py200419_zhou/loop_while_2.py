"""
while loop <-> for loop
"""

# summary of from 1 to 100

sum = 0

num = 1

# sum + num -> sum

while num <= 100:
    sum += num
    num += 1

print("sum is {}".format(sum))



# summary of from 2 + 4 + 6 + ..... 200

sum = 0
counter = 0 # 0-99
num = 1

# sum + num -> sum
while counter < 100:
    counter += 1
    num = counter * 2
    sum += num

print("sum is {}".format(sum))
