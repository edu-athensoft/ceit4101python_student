"""
function argument
variable arguments

default argument and non-default argument
"""


def greeting(name, greeting="Good morning"):
    print("{}, {}!".format(greeting, name))

# 1 arg
greeting('Marie')
greeting('Peter')
greeting('White')

# 2 args
greeting("Sarah", "Good evening")


# special case
# rule: non-default argument must stay before default argument

"""
def greeting2(greeting="Good morning", name):
    print("{}, {}!".format(greeting, name))


def greeting3(greeting="Good morning", name, age=14):
    print("{}, {}, {}!".format(greeting, name, age))


def greeting3(age, greeting="Good morning", name):
    print("{}, {}, {}!".format(greeting, name, age))
"""