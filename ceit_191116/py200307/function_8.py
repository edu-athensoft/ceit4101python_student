"""
function and return and if-else

best practices

"""

"""
check a number and tell if it is a positive, zero or negative number
"""


def get_sign(num):
    result = ''
    if num > 0:
       result ='Positive'
    elif num == 0:
        result = 'Zero'
    else:
        result = 'Negative'
    return result

num = 0
result = get_sign(num)

print("The number {} is {}".format(num, result))
print("Le nombre de {} es {}".format(num, result))
print("数字 {} 是 {}".format(num, result))
