"""
mini project: calculator with input
"""

# task: define a function to add two numbers
def add(n1, n2):
    return n1+n2

# task: define a function to subtract two numbers
def sub(n1, n2):
    return n1 - n2

# task: define a function to multiply two numbers
def mul(n1, n2):
    return n1 * n2

# task: define a function to divide a number with another one
def div(n1, n2):
    return n1 / n2

# task: define a function to evaluate an arithmetic expression

# (3+5)*(2-4)
def eval_expr(expr):
    return eval(expr)


# init
# input part of the program

option = input("Please choose an operation [add,sub,mul,div,expr]:")

result = None

if option == 'expr':
    expr = input("expr = ")
    result = eval_expr(expr)
else:

    if option != 'add' and option != 'sub' and option != 'mul' and option != 'div':
        result = "Wrong input, please try it again!"
    else:
        n1 = float(input("n1 = "))
        n2 = float(input("n2 = "))
        if option == 'add':
            result = add(n1, n2)
        elif option == 'sub':
            result = sub(n1, n2)
        elif option == 'mul':
            result = mul(n1, n2)
        elif option == 'div':
            result = div(n1, n2)
        else:
            print("error cases!")

print(result)



"""
if option == 'add':
    n1 = float(input("n1"))
    n2 = float(input("n2"))
    result = add(n1,n2)
    print(result)
elif option == 'sub':
    n1 = float(input("n1"))
    n2 = float(input("n2"))
    result = sub(n1, n2)
    print(result)
elif option == 'mul':
    n1 = float(input("n1"))
    n2 = float(input("n2"))
    result = mul(n1, n2)
    print(result)
elif option == 'div':
    n1 = float(input("n1"))
    n2 = float(input("n2"))
    result = div(n1, n2)
    print(result)
elif option == 'expr':
    expr = input("expr")
    result = eval_expr(expr)
    print(result)
else:
    result = "Wrong input, please try it again!"
    print(result)
"""

