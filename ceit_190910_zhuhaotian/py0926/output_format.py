# format()
# case 1. default index 0, 1
x = 5
y = 4

print('Row: {}, Col: {} the value is correct.'.format(x,y))

x = 6
y = 3

print('Row: {}, Col: {} the value is correct.'.format(x,y))

# case 2. specified index
x = 5
y = 4
z = 9

print('Row: {1}, Col: {0} z:{2} the value is correct.'.format(x,y,z))

# case 3. named index
x = 5
y = 4

print('Row: {row}, Col: {col} the value is correct.'.format(row=x,col=y))