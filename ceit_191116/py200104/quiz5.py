"""
quiz5
"""

# define, create, declare
my_list = [1,2,3,4,5,6]
# print(my_list[0])
# print(my_list[5])
# print(my_list[-1])
print(my_list[0], my_list[5])
print(my_list[0], my_list[-1])

# change value
my_list[3] = 999
print(my_list)

#
my_tuple = (1,2,3,4,5,6)
print(my_tuple[0], my_tuple[-1])

#
# my_tuple[3] = 999

# define a set
my_set = {1, 1, 2, 2, 3, 3}
print(my_set)

# define a dictionary
a = 'q1'
b = 'q2'
c = 'q3'
d = 'q4'
my_dict = {
    a : 100,
    b : 200,
    c : 300,
    d : 400
}
print(my_dict)
# print(a,my_dict[a])
my_dict[b] = 220
print(my_dict)

# my_dict = {1: 100,2: 200,'c': 200}

print(my_dict)


# type conversion
# float -> str
f1 = 1.5
print(str(f1), type(str(f1)))
print(int(f1))

# str -> int
s1 = "300"
int(s1)
print(s1)


# try set
set1 = {'a','b','c'}
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)









