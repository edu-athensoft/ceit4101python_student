"""
Print out all the even numbers from 0 to 100
"""

# solution 1
for i in range(100):
    if i % 2 == 0:
        print("number {}".format(i))

# solution 2
for i in range(0, 100, 2):
    print("number {}".format(i))

