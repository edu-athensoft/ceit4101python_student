"""
review literal- string
"""

# output: I'm a programmer.

# solution 1
str1 = "I'm a programmer."
print(str1)

str1 = 'aaaa"bbbb'
print(str1)

# solution 2 - escape character
str2 = 'I\'m a programmer.'
print(str2)

# solution 3 - raw string
str3 = r"I'm a programmer."
print(str3)

str3 = r"I'm a programmer."
print(str3)

str4 = r"\u253bxxxxx"
print(str4)

str4 = "\u253bxxxxx"
print(str4)

str5 = u"\u253b    \u2531"
print(str5)

# multiline string
mstr = """
asdfasdf
asdfkljasdfk
    asdkfkasdfasd
"""
print(mstr)

# application

