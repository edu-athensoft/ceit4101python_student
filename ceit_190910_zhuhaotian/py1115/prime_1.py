"""
input a number

number % 2 == 0 ?
number % 3 == 0 ?
number % 4 == 0 ?
...
number % number-1 ==0 ?

if there exists at least ONE case of perfect division,
then the number is NOT a prime number
and the loop terminates

2..number-1


output result 'The number {} is/is not a Prime Number'
"""

num = 10

for i in range(2,num):
    if num % i == 0:
        print("{} is not a Prime Number.".format(num))
        break
else:
    print("{} is a Prime Number.".format(num))

