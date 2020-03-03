"""
prime number
"""


num = int(input("please input a positive integer: "))

for i in range(2,num):
    # print(i)
    if num % i == 0:
        print("{} is not a prime number and it can be perfectly divided by {}.".format(num,i))
        break
else:
    print("{} is a prime number.".format(num))



if True:
    pass
else:
    pass

def myfoo():
    pass


