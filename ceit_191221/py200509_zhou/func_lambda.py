"""
lambda, anonymous

lambda arguments: expression
"""

def foo(x):
    print("test foo({})".format(x))

foo(1)
foo(2)
foo(3)
print()

# lambda
double = lambda x: 2*x
print(double(3))
print()

#
def double(x):
    return x * 3
print(double(3))


