"""
output formatting
print() -> output formatting
string template, pass in values(arguments)
string template includes placeholder(s)

format()
"""

# case 1
print("Hello, Peter. How are you? ")
print("Hello, Adam. How are you? ")
print("Hello, Alex. How are you? ")
print("Hello, Mary. How are you? ")
print()

# case 2
print("Hello, {}. How are you? ".format("Peter"))
print("Hello, {}. How are you? ".format("Adam"))
print("Hello, {}. How are you? ".format("Alex"))
print("Hello, {}. How are you? ".format("Mary"))
print()

# case 3
name = 'Adam'
print("Hello, {}. How are you? ".format(name))