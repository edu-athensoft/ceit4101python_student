"""
quiz 10-3
"""

score = (85, 78, 96, 85, 73, 59, 95)

number_of_A = 0

total_score = 0
for s in score:
    total_score += s
    if s >= 90:
        number_of_A += 1

average_score = round (total_score / len(score) , 2)

print("The average_score is {}".format(average_score))
print("There is(are) {} student(s) in this class got an A".format(number_of_A))

# 74.43
# 74.4
# 74






