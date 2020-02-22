"""
quiz_10_q3
"""
# calculate the average score of all students
# and count number of students who got grade A

# method : tuple
students = (("Marie", 85),
            ("Phoebe", 78),
            ("Sabrina", 96),
            ("Emma", 90),
            ("Amy", 73),
            ("Isabelle", 59),
            ("Clark", 45))
total_score = 0
num_of_student = len(students)
num_of_grade_a = 0
SCORE_GRADE_A = 90
student_of_grade_a = []

for student_entry in students:
    total_score += student_entry[1]
    #num_of_student += 1
    if student_entry[1] >= SCORE_GRADE_A:
        num_of_grade_a += 1
        student_of_grade_a.append(student_entry)

student_of_grade_a = tuple(student_of_grade_a)
average_score = total_score/num_of_student
print("The average score is {:4.1f}".format(average_score))
print("The number of students got grade A is {}".format(num_of_grade_a))
print("Grade A students and scores: {}".format(student_of_grade_a))
print()


