"""
datatype conversion 2
"""

# set()
# list -> set
list1 = [1,2,1,2,3]
set1 = set(list1)
print(set1)

# tuple -> set
tuple1 = (1,2,1,2,3)
set1 = set(tuple1)
print(set1)

# set -> tuple
# tuple()
set1 = {1,2,3}
tuple1 = tuple(set1)
print(tuple1)

# set -> list
# list()
set1 = {1,2,3}
list1 = list(set1)
print(list1)

# list -> tuple
list1 = [1,2,1,2,3]
print(tuple(list1))

# tuple -> list
tuple1 = (1,2,1,2,3)
print(list(tuple1))

# To convert to dictionary, each element must be a pair
# dict()
list_d = [[1,'Peter'],
           [2,'Nana'],
           [3,'Sarha']]
print(dict(list_d))

tuple_d = ([1,'Peter'],
           [2,'Nana'],
           [3,'Sarha'])
print(dict(tuple_d))

tuple_d2 = ((1,'Peter'),
            (2,'Nana'),
            (3,'Sarha'))
print(dict(tuple_d2))


# dict -> list or tuple
dict1 = {1: 'Peter', 2: 'Nana', 3: 'Sarha'}
print(list(dict1))
print(tuple(dict1))
print(set(dict1))