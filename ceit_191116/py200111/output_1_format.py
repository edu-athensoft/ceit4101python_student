"""
output formatting
string  format()
string template
"""

greeting = "Hello, Athens. How are you?"
# print(greeting)

greeting = "Hello, Helen. How are you?"
# print(greeting)

greeting = "Hello, Marie. How are you?"
# print(greeting)

greeting = "Hello, Cindy. How are you?"
# print(greeting)

# placeholder
name1 = 'Obama'
name2 = 'Helen'
name3 = 'Marie'
name4 = "Cindy"

greeting1 = "morning!"
greeting2 = "afternoon!"
greeting3 = "evening!"

print("Hello, {}! How are you?".format(name1))
print("Hello, {}! How are you?".format(name2))
print("Hello, {}! How are you?".format(name3))
print("Hello, {}! How are you?".format(name4))

print("Good {}, {}! Long time no see".format(greeting1, name1))
print("Good {}, {}! Long time no see".format(greeting2, name2))
print("Good {}, {}! Long time no see".format(greeting3, name3))

print("Good {}, {}! Long time no see".format(name3,greeting3))

