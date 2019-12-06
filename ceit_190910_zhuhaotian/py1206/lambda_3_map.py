# lambda function
# map

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = list(map(lambda x: x**2, my_list))
print(new_list)


sqr = lambda x: x**2
new_list = list(map(sqr, my_list))
print(new_list)