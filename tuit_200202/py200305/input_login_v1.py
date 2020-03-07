"""
Login Form ver 1.0

User can input his/her name
User can input his/her password
The system responds with a message like:
   Welcome xxx ! Your password is yyy
print out 'Bye!'
"""

print("==== Login Form ====")

# 1st part: to accept input
name = input("Your name:")
password = input("Your password:")

# 2nd part: processing

# 3rd part: output
print('Welcome {}! Your password is {}'.format(name, password))

print("Bye!")
