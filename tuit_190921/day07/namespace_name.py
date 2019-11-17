# namespace

# case 1
a = 2
print(a, id(2))
print(a, id(a))
print()

# case 2
a = 2
print('id(a)=',id(a))

a = a+1
print('id(a)=',id(a))
print('id(3)=',id(3))

b = 2
print('id(b)=',id(b))
print('id(2)=',id(2))