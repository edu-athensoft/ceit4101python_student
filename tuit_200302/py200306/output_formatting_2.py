"""
output formatting
"""

print("Hello {0}, your balance is {1:9.3f}".format("Adam", 230.2346))

# how to just keep 2 decimal places
print("Hello {0}, your balance is {1:9.2f}".format("Adam", 230.2346))

# how to allocate 10 spaces to display Adam
print("Hello {0:10}, your balance is {1:9.3f}".format("Adam", 230.2346))

# name -> Adam
# balance -> 230.2346
# positional arguments -> keyword arguments
print("Hello {0}, your balance is {1:9.3f}".format("Adam", 230.2346))
print("Hello {name}, your balance is {balance:9.3f}".format(name="Adam", balance=230.2346))

