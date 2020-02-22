"""
while loop ex2
"""

# sum =   1+2+3+......+ 50 +   60+61+.....+ 100

# using while loop

"""
sum_lost = 0
for i in range(51,60):
    sum_lost += i
print(5050-sum_lost)
"""

# 4555

"""
test expression:     1<= i <= 50  or  60<= i <= 100
while body:      sum = sum + i
"""
# i = 1
# while i <= 50 or ( 60 <= i and i<=100):
#     sum = sum + i
#     i += 1
#     # if i>100:
#     #     ........

i = 1
summary = 0
while i< 101:
    if i <= 50 or (60 <= i and i<=100):
        summary += i
    i += 1

print("The sum is {}".format(summary))



