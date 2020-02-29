"""
review datatype
"""

# number
# integer, float, complex
i1 = 123
i2 = 0b1
i3 = 0xf
print(i1, type(i1))
print(i2, type(i2))
print(i3, type(i3))

f1 = 1.23
print(f1,type(f1))

f2 = 1.23e5
print(f2,type(f2))

f3 = 1.23e-3
print(f3, type(f3))


# string
s1 = 'hello 1'
print(s1, type(s1))

s2 = "hello 2"
print(s2, type(s2))

# collection - list
list1 = [1,2,32,3454,5,67]
print(list1, type(list1))

list2 = [1,"32",True]
print(list2, type(list2))

list3 = [['Ming',85], ['Hong',90], ['Qiang',70]]          # nested list
print("len of list3 is ",len(list3))
print("len of list3[0] is", len(list3[0]))

# collection - tuple
tuple1 = (200,100)
print(tuple1, type(tuple1))

tuple2 = (('Ming',85), ('Hong',90), ('Qiang',70))
print(tuple2, type(tuple2))

# mix - list and tuple
mix = [('Ming',85), ('Hong',90), ('Qiang',70)]

# set - unordered collection of unique items
set1 = {'1','2','3','4','5'}
print(set1, type(set1))

set2 = {'1','1','3','4','5'}
print(set2, type(set2))

# dictionary - key-value pair
# https://www.abc.com/app/login?username='xxxxx'&password='abc123'
# dict
client1 = {
    'first_name' : 'Peter',
    'last_name' : 'White',
    'file_date' : '2020-02-02',
    'forward_balance' : 0,
    'transaction' : 'deposit',
    'debit_amt' : 5000
}
print(client1, type(client1))