"""
string formatting
"""

# case 1
print("Hello {0}, your balance is {1:9.3f}".format("Adam", 230.2346))
print("Hello {0}, your balance is {1}".format("Adam", 230.2346))
print("Hello {0}, your balance is {1:4.3f}".format("Adam", 230.2346))
# print("Hello {0}, your balance is {1:9.3s}".format("Adam", 230.2346))
# f: float

print()

# case 2
print("Hello {name}, your balance is {blc:9.3f}".format(name="Adam", blc=230.2346))

