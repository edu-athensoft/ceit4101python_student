"""
output syntax
template.format(p0, p1, ..., k0=v0, k1=v1, ...)
"""
a = 1
b = 2
c = 3

print("asdfsadk {1} asdflasdf {0} asdfdasf {2}".format(a, b, c))

print("{1} {2} {0} asdfsadk {c} asdflasdf {b} asdfdasf {a}".format(a, b, c, a=a, b=b, c=c))


