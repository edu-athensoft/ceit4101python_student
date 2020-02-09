"""
a student wrote an exam,
if the score is >= 90, he will get the grade of 'A'
if the score is >= 80, he will get the grade of 'B'
if the score is >= 70, he will get the grade of 'C'
if the score is >= 60, he will get the grade of 'D'
if the score is >= 1, he will get the grade of 'F'
if the score is 0 , he will get the comment of 'Absent'

write a program to calculate the grade for this student with a given score
"""

score = float(input("Enter the score [float]: "))

grade = ''
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 1:
    grade = 'F'
else:
    grade = 'Absent'

print("You got a grade of {}!".format(grade))



