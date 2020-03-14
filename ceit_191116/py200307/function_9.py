"""
function
return multiple objects
"""


def double(a, b):
    return 2*a, 2*b


result_1, result_2 = double(1, 2)
print(result_1)
print(result_2)

result_1, result_2 = double('a', 'b')
print(result_1)
print(result_2)