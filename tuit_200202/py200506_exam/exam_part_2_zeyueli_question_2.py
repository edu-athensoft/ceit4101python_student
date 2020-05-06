# question 2
# i will create a list with all the characters in the given string and check how many of them there are with a for loop.
string = input("Input a string literal")
list = []
a = 0
for i in string:
    if not i in list:
        list.append(i)
for i in list:
    a = 0
    for j in string:
        if j == i:
            a += 1
    print("There are {} of {}".format(a, i))