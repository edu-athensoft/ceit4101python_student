"""

"""

import re

# float_number = str(input(“Please input the number:”))
float_number = "-4e3"
value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

result = value.match(float_number)

if result:
    print("Number is a float.")

else:
    print("Number is not a float.")
