"""
recursion and recursive function
"""



def foo2():
    global counter
    print("f2 "+str(counter))
    counter += 1
    foo2()


counter = 1
foo2()



