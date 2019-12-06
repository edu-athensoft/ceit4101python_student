# def outer_function():
#     b = 20
#     def inner_func():
#         c = 30
#
# a = 10

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a, id(a))

    inner_function()
    print('a =', a, id(a))


a = 10
outer_function()
print('a =', a, id(a))