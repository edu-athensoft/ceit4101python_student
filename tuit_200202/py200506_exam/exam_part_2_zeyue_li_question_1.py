# question 1
string = input("Input a string literal:")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new_string = ''
for i in string:
    if i not in punctuations:
        new_string += i
print(new_string)
