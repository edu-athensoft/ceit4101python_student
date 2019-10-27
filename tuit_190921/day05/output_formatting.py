# output formatting
# string.format()

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x, y))

print('The value of y is {1} and x is {0}'.format(x, y))

my_name = 'White'
print('Hello {name}, {greeting}'.format(greeting = 'Good morning!', name = my_name))

# using %
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %4.2f' %x)
print('The value of x is %5.2f' %x)
print('The value of x is %6.2f' %x)
print('The value of x is %7.2f' %x)
print('The value of x is %8.3f' %x)
