"""
project login
"""

# expected credentials
USER_NAME = 'admin'
PASSWORD = '12345'

print("=== Login Form ===")

while True:
    username = input("User name:")
    if username.lower() == 'q' or username.lower() == 'quit':
        print("Bye!")
        break

    password = input("password:")

    if username == USER_NAME and password == PASSWORD:
        print("Hello, {usr}! Your password is {pwd}".format(usr=username, pwd=password))
        break
    else:
        print("Access denied. please try again!")

