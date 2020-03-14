"""
project login form
only accept 3 times of try, otherwise quit/lock
"""

# expected credentials
USER_NAME = 'admin'
PASSWORD = '12345'
TRY_TIMES = 3

print("=== Login Form ===")

count = 0
while count < TRY_TIMES:
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
        count += 1
else:
    print("You've tried for 3 times already. Bye!")

