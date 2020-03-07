"""
function
variable arguments
"""

def greet(name = "Peter",msg = "Good morning!"):
    print("Hello", name + ', ' + msg)


# call function
greet("Mary", "Good Evening")
greet(msg="Good Evening",  name="Mary")

