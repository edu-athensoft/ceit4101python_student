"""
lambda map
map()
"""

# regular
my_list = [1,2,3,4,5,6,7,8,9]
double_list = []

for i in my_list:
    double_list.append(i * 2)

print("original list {}".format(my_list))
print("doubled list {}".format(double_list))
print()

# list()
result_map = map(lambda x: x*2, my_list)
print(result_map, type(result_map))
print(list(result_map))

# compact
print(list(map(lambda x: x*2, my_list)))