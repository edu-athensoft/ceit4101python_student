"""
global variable
global scope
local scope
"""

def foo():
    print(a)       # the global vars are visible in local scope
    print(str1)
    print(mylist)
    # a = a +1    # cannot write global variable directly




a = 1
str1 = "abc"
mylist = [1,2,3]

foo()