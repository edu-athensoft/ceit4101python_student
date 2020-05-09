"""
global variable
local scope
"""

def foo():
    x = 1
    print(x)
    x = 2 * x
    print(x)

x = -1
foo()
print("x=", x)