"""
function
with parameters
reusable and reusebility

quality of a software/code
- reusebility
- readability
- maintainability
"""

print("+===============================================+")
print("| TITLE     \t | NAME     \t  |    SCORE   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print("=================================================")

print("END OF ORIGINAL GRID\n\n\n")

# function:       print out the grid line
# function name:  print_line
# arguments:      styled_line

def print_line(styled_line):
    print(styled_line)

STYLED_LINE_0 = '================================================='
STYLED_LINE_1 = '+===============================================+'
STYLED_LINE_2 = '+-----------------------------------------------+'

# test
# print("test")
# print_line(STYLED_LINE)

print_line(STYLED_LINE_1)
print("| TITLE     \t | NAME     \t  |    SCORE   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_2)
print("| AAAAA     \t | N001     \t  |    100.0   \t|")
print_line(STYLED_LINE_1)


