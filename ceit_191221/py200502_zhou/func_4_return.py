"""
function - return
"""

# return without data
def foo():
    print("asdkfjas1")
    print("asdkfjas2")
    return
    print("asdkfjas3")


foo()
print()


# return with data
def max(a,b):
    result = a
    if a < b:
        result = b
    return result

print(max(1,2))


# return result of expression
def shownum(x):
    return 2*x

num = shownum(3)
print(num)


# return a specified value
def shownum2():
    return 2

print(shownum2())


# return multiple values
def showKV(key,value):
    return "K-"+key, "V-"+value


k,v = showKV("Mon","Monday")
print("Key is {} and Value is {}".format(k, v))
print("Key Value Pair is {}:{}".format(k, v))


# Special case
x = foo()
print(x, type(x))
