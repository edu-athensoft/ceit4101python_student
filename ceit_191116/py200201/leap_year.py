# test if a year is a leap year

year = input("Enter a number for a year:")

year = int(year)

# nested if-else statement
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is leap year".format(year))

else:
    print("{} is not a leap year".format(year))

print("END.")
