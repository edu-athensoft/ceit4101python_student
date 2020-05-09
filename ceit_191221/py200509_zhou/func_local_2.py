"""
using global variable in local scope
"""

def foo():
    global x
    x = x + 1
    print(x)


x = 10
foo()
print("x in global is {}".format(x))