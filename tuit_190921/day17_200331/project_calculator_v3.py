"""
mini project: calculator with input
version: 3.0
author: Athens
date:   2020-03-31

description:
if user input 'q', the program comes to end
if user input other words, the program will run again and again
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

while True:
    option = input("Please choose an operation [add,sub,mul,div,expr](enter 'q' to exit):")
    result = None

    if option != 'add' and option != 'sub' and option != 'mul' and option != 'div':
        if option =='q':
            break
        else:
            result = "Wrong input, please try it again!"
    elif option == 'expr':
        expr = input("expr = ")
        result = eval_expr(expr)
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

