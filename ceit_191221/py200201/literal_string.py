"""
python literal
string
"""

# case 1 - using double or single quote
str1 = "Hello kitty!"
str2 = 'Mickey'

print(str1, str2)

# case 2 - multiple line string
mstr1 = """aksjdfakasdjf
alsdfjkas
alsdfjas
alsdkfjlasdf
alsdfj"""

print(mstr1)

mstr2 = '''AAAAAAAAA
alsdfjkas
alsdfjas
alsdkfjlasdf
alsdfj'''

print(mstr2)

# case 3 - one character
mychar1 = 'C'
mychar2 = "X"
print(mychar1, mychar2)


# case 4
# output copyright symbol
ustr1= u"copyright symbol \u00A9 \u00A7 \u00A7"
print(ustr1)


# case 5 - escaped char
print("aaaa bbbb")
print("aaaa \n bbbb")
print("cccc \t bbbb")

# output an arbitary string containing one ', ", \
print("aasf\'djkasjf\"laskdfsa\\klf")

# case 6 - raw string
rawstr = r"aasf\'djkas\u00A9 \u00A7 \u00A7jf\"laskdfsa\\klf"
print(rawstr)
