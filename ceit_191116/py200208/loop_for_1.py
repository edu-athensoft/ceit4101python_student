"""
for-loop
"""

"""
for val in sequence:
	Body of for
"""

my_list = [1,2,3,4,5,6,7,8,9,14,4,57,8,9,0]
for i in my_list:
    i +=0.5
    print("modified list item is {}".format(i))

print("============")

my_tuple = (1,2,3,4,5,6,7,8,9,14,4,57,8,9,0)
for i in my_tuple:
    i *=0.5
    print("modified list item is {}".format(i))

print("============")

my_string = "Hello world!"
for i in my_string:
    print("modified list item is {}".format(i))





