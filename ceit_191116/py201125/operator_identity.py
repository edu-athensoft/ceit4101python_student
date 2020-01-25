"""
identity operator
is, is not
"""

x1 = 5
y1 = 5
# Output: True
print(x1 is y1)
print(id(x1),id(y1))

x2 = 'Hello'
y2 = 'Hello'
# Output: True
print(x2 is y2)
print(id(x2),id(y2))

x3 = [1,2,3]
y3 = [1,2,3]
# Output: False
print(x3 is y3)
print(id(x3),id(y3))
