"""
Truncating strings with format()
"""

# truncating strings to 3 letters
print("{}".format("caterpillar"))
print("|{:.3}|".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("|{:5.3}|".format("caterpillar"))


# truncating strings to 3 letters,
# padding and center alignment
print("|{:^5.3}|".format("caterpillar"))
print("|{:*^7.3}|".format("caterpillar"))
