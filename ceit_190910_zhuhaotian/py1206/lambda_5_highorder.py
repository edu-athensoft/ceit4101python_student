def my_func(f, n):
    return f(n)


f0 = lambda x: x*2
f1 = lambda x: x*3
f2 = lambda x: x*4

print(my_func(f0, 5))
print(my_func(f1, 5))
print(my_func(f2, 5))
