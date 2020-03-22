"""
mini project: calculator
"""

# task: define a function to add two numbers
def add(n1, n2):
    return n1+n2

# task: define a function to subtract two numbers
def substract(n1, n2):
    return n1 - n2

# task: define a function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# task: define a function to divide a number with another one
def divide(n1, n2):
    return n1 / n2

# task: define a function to evaluate an arithmetic expression

# (3+5)*(2-4)
def eval_expr(expr):
    return eval(expr)


# init
# input part of the program
n1 = 1
n2 = 2

my_expr = '2+3*4'

# processing part
result_a = add(n1,n2)
result_s = substract(n1, n2)
result_m = multiply(n1, n2)
result_d = divide(n1, n2)

result_expr = eval_expr(my_expr)

# output part
print(result_a)
print(result_s)
print(result_m)
print(result_d)
print(result_expr)