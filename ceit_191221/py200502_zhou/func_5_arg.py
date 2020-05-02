"""
argument and parameter

fixed number of arguments
positional argument
"""

# zero parameter
def foo1():
    print("foo1()")


# one parameter
def foo2(a):
    print("foo2({})".format(a))


# two parameters
def foo3(x,y):
    print("foo3({},{})".format(x,y))


foo1()
foo2(9)
foo3(6,9)
print()

# missing required positional argument(s)
# foo3(8)

# takes 2 positional arguments but 3 were given
foo3(8,8,9)



