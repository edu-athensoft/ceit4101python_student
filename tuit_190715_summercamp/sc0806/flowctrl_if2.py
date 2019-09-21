# if-else

# weather = True
is_sunny = True

# if weather:
if is_sunny:
    print("I go out for shopping.")
else:
    print("I stay at home.")
print("bye")

# ==================================

day_of_week = 'Sun'
if day_of_week == 'Tues':
    print("I go for movie")
else:
    print("I go for shopping")
print("bye")

# ==================================
# problem:  to tell a number whether it is an Odd or Even

# step1. input
number = input("Enter an integer:")

# step2. processing
number = int(number)
if number%2 == 0:
    print("The number of {} is Even".format(number))
else:
    print("The number of {} is Odd".format(number))

# step3. output
print("bye")


