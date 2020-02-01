"""
flow control
if-elif-else
"""

# 90 -> A
# 80 -> B
# 70 -> C
# 60 -> D
# <60 -> F
# 0 -> ABSENT

"""
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
"""

print("=== Student Grade System ===")
# input
score = int(input("Enter your score [integer]:"))
# print("score =",score)
# business logic, get grade
grade = 'ABSENT'
if score >=90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
elif score >= 1 :
    grade = 'F'
else:
    pass
# output
print("You got a grade of {}".format(grade))




