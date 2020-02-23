"""
project 1. Student Grading System
"""

# step 1. print out the whole grid (data)

a = ['Peter',89]
print(a[0],a[1])

if a[1] >= 90:
    pass


# students =

# a0 = ['Peter',89]
# a1 = ['Mary',70]
# a2 = ['Sarah',56]

# students = [a0, a1, a2]

# magic number, value


students = [('Peter',96),
            ('Mary', 70),
            ('Sarah', 92)]

# GRADE_A_SCORE = 95
GRADE_A_SCORE = 90

winners = []

for stu in students:
    if stu[1] >= GRADE_A_SCORE:
        winners.append(stu)

print("The winners name list is {}".format(winners))
winners = tuple(winners)

print("The winners name list is {}".format(winners))
