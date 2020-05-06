"""
My idea is to input a string, then put the output in a form of a dictionnary.
I will count the caracters of the string in a loop then and print it out.
"""
x = input('Please enter a string:')
y = {}
for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
print ("Count of all characters in your string is :\n ",str(y))
