# case 1

is_sunny = True
has_money = True

if not is_sunny:
    print("I stay at home")
elif has_money:
    print("I go shopping")
else:
    print("I stay at home")

# case 2
number = 6

if number < 3:
    print("{} is a small number".format(number))
elif number < 6:
    print("{} is a medium number".format(number))
else:
    print("{} is a big number".format(number))
