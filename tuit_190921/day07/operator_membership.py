# operator membership

# case 1 - string
a = 'hello'
print('h' in a)

b = [1,2,3,'a','b','c']
print(4 in b)
print(4 not in b)

c = (1,2,3,4,5)
print(5 in c)
print(2 not in c)

d = {3,4,5,6,7,8}
print(3 in d)
print(3 not in d)

e = {1:'a', 2:'b'}
print(1 in e)
print(2 in e)
print('a' in e)     # 'a' is not a key
print('b' in e)     # 'b' is not a key

e = {1:'a', 2:'b', 'a':1, 'b':2}
print(1 in e)
print(2 in e)
print('a' in e)     # 'a' is  a key
print('b' in e)     # 'b' is  a key



