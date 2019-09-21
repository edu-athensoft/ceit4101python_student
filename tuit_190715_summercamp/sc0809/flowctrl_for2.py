# to calculate the average score

score_list = [95, 91, 82, 78, 88, 67, 80, 50]
num = len(score_list)  # to avoid magic number

total_score = 0
# total score / num
# to calculate the total score
for score in score_list:
    total_score = total_score + score

# to calculate the average
avg_score = total_score / num

# output the result
print("The average score of students: {} is {}.".format(score_list, avg_score))





