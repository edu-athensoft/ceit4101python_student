# Quiz 1 - Python fundamental

'''
Question 5. Verify your password

User is often asked to set a password during registration.
User needs to input twice (1 for password, and the other for re-input password)
You are asked to write a program to verify if the user inputs the same password.
Print out the results in proper way
Hint:
Just return the boolean value using the proper comparison operator.
'''

password1 = input("Please enter the password:")
password2 = input("Please enter the password again:")

result = password1 == password2
print("The password you have input for twice is identical.  {}".format(result))

