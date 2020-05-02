"""
function argument

arbitrary argument
"""

# *names,  name

# *name,   names

# *names as tuple
def foo(*names):
    print(names,type(names))
    for name in names:
        print(name, end="\t\t")


foo("name1","name2","name3","name4","name5")



