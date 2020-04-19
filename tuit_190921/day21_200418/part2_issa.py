# program 1
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

user_str = input("Write your string and I will remove the punctuation: ")

no_punct = ""
for characters in user_str:
    if characters not in punctuation:
        no_punct = no_punct + characters

print(no_punct)

# program 2
"""
# plan:
1. import from data type of Dictionary (collections(Counter)) 
2. input the string
3. count the number of each character using the data type.
4. print the result
"""
# program:
from collections import Counter

user_str = input("Write your string and I will count the number of time each character is occurring: ")
counting = Counter(user_str)
print("The number of time each character is occurring is: {}".format(counting))

# program 3
"""
# plan
1. import from data type of Dictionary (itertools(combinations))
2. user input
3. run all the possible combinations of the user input
4. output all the combinations (print it)
"""


