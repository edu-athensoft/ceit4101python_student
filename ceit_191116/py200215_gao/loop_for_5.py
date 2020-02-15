"""
for loop
print out a multiplication table
step 1.
12 X 1
12 X 2
12 X 3
...
12 X 12


step 2.
12 X 1 = 12
12 X 2 = 24
12 X 3 = 36
...
12 X 12 = 144

"{}".format()

i = [1,.....,12]
range(1,13)
"{} x {} = {}".format(12, i, 12*i)

"""

# "string template"
# Hello Mary, how are you?
# Hello Marie, how are you?
# "Hello {}, how are you".format("Mary")
# "Hello {}, how are you".format("Marie")


"""
12 X  1 =  12
12 x 10 = 144



"""


print("{0} x {1:>2} = {2:>3}".format(12, 1, 12*1))
print("{a} x {b:>2} = {result:>3}".format(a=12, b=10, result=12*10))





