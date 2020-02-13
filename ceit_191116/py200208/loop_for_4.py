"""
production level code
input a stop number as the upper limit number
and print out all the even numbers from 0 to the given number from keyboard

robust, reliability
covering test path
advantages and disadvantages of algorithms
loop + branching
"""

# solution 2
stop_num = int(input("Please enter a positive integer:"))

if stop_num < 0:
    print("Invalid input, please enter again")
elif stop_num == 0:
    print("even number is {}".format(stop_num))
else:
    for i in range(0, stop_num, 2):
        print("even number {}".format(i))

print("bye")

