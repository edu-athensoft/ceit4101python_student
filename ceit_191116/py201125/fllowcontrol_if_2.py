"""
flow control
if-else
"""
is_good_weather = True

if is_good_weather:
    print("Hang out for shopping.")
else:
    print("Watch movie at home")


# test if a given number is a positive/zero or negative number
# using input()
# string.isDigit()
# https://blog.csdn.net/bug_moving/article/details/52886412
# https://www.runoob.com/python3/python3-check-is-number.html


my_input = "5.67"
# print(my_input.isdigit())
# print(my_input.index("."))

# 5
# -5
# 5.6
# -5.6
# 5e2
# 5e-2

# if your input is not a numeric compatible literal
# print out a text warning
# else

my_num = float(my_input)
if my_num>=0 :
    print("Positive and Zero")
else:
    print("Negative")
