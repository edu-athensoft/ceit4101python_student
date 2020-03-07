"""
project:
input 2 numbers
and print out the summary of the input
"""

# the title of the software
print("==== Adding two numbers ====")

# accepting inputs
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

# processing
num1 = float(num1)
num2 = float(num2)
summary = num1 + num2

# output
print("The summary of {} and {} is {}.".format(num1, num2, summary))
print("Done.")