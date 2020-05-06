x = input('Please enter a string:')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
y = ""
for i in x:
    if i not in punctuations:
        y += i
print(y)

