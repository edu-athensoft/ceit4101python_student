"""

"""

# scores = ([1])

scores = [('Marie',85),('Phoebe',78),('Sabrina',96),('Clark',93)]

# scores = (85,78,96)

# formula of avg = sum of score/len
sum = 0
size = len(scores)
num_a = 0

for stu in scores:
    # print(stu)
    sum += stu[1]
    if stu[1] >=90:
        num_a += 1
        print(stu)

print(sum)

avg = sum/size
print("avg = {:.2f}".format(avg))

print("There are {} students who got A.".format(num_a))

