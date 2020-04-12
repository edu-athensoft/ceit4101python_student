"""
flow control
nested if statement
"""


# check a number from Zero, Positive or Negative
number = int(input("Enter an integer:"))

if number > 0:
    print("Positive")
else:
    if number < 0:
        print("Negative")
    else:
        print("Zero")

