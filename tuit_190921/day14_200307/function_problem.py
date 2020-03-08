"""
function - problem of reuse
"""

# print("+-----------+")
# print("| 1  |  a   |")
# print("+-----------+")
# print("| 2  |  b   |")
# print("+-----------+")


# define a function
def print_table():
    print("+-----------+")
    print("| 1  |  a   |")
    print("+-----------+")
    print("| 2  |  b   |")
    print("+-----------+")

# call a function
# print_table()
# print_table()
# print_table()

for i in range(30):
    print_table()