"""
output formatting
string  format()
positional arguments
"""
name1 = 'Obama'
name2 = 'Helen'
name3 = 'Marie'
name4 = "Cindy"

greeting1 = "morning!"
greeting2 = "afternoon!"
greeting3 = "evening!"

print("Good {1}, {0}! Long time no see".format(name3, greeting3))

print("Good {2}, {0} and {1} ! Long time no see".format(name3, name4, greeting3))