"""
identity:  is, is not
"""

# case 1: numeric
x1 = 5
y1 = 5
result = x1 is y1
print("is x1:{} identical to y1:{}? Answer is: {}".format(x1,y1,result))

result = x1 is not y1
print("is x1:{} identical to y1:{}? Answer is: {}".format(x1,y1,result))


# case 2: string
x2 = 'abc'
y2 = 'abc'
result = x2 is y2
print("is x2:{} identical to y2:{}? Answer is: {}".format(x2, y2, result))

result = x2 is not y2
print("is x2:{} identical to y2:{}? Answer is: {}".format(x2, y2, result))


# case 3: collection object
x3 = [1,2,3]
y3 = [1,2,3]
result = x3 is y3
print("is x3:{} identical to y3:{}? Answer is: {}".format(x3, y3, result))

x3 = []
y3 = []







