"""
typical local scope
"""

# local var in for-loop
for y in range(10):
    print(y*2, end="\t\t")

print("====")

# loca var as function parameter / in a function

def foo(y):
    print(2 * y)

foo(6)
