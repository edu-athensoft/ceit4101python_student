"""
output formatting
"""

a = 1
b = 2
c = 3

print("asdfsadk {} asdflasdf {} asdfdasf {}".format(a, b, c))

print("asdfsadk {1} asdflasdf {0} asdfdasf {2}".format(a, b, c))

print("asdfsadk {c} asdflasdf {b} asdfdasf {a}".format(a=a, b=b, c=c))