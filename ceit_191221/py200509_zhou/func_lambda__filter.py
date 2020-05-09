"""
lambda filter
filter()
"""

# select odd numbers
my_list = [1,2,3,4,5,6,7,8,9]

result = []
for i in my_list:
    if i%2 == 1:
        result.append(i)

print("original list is {}".format(my_list))
print("filtered list of odd number is {}".format(result))
print()


# filter() using lambda
res_filter = filter(lambda x: x%2 ==1, my_list)
print(type(res_filter), res_filter)

# list()
print(list(res_filter))

# compact
print(list(filter(lambda x: x%2 ==1, my_list)))


