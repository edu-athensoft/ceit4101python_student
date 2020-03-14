"""
Project: Login Form v1
The form accepts a username and a password
then you output the username and password
echo
"""

# option 1 - directly output
# print(input("Your name:"))
# print(input("Your password:"))


# option 2 - in regular way
name = input("Your name:")
password = input("Your password:")

name = '0001-'+name

# print(name, password)
print("Your name is ",name, " Your password is ", password)