"""
identifier
"""

# rule 1 - valid char
# [a-z][A-Z]_[0-9]

# rule 2 - start with [a-z][A-Z]_
_123 = "my string"
__123 = "your string"
a123 = "ok"
A123 = "ok"

# 01 = 1
# 9 = "abc"
# 01abc = 2
# 02_abc = 5


# rule 3 - do not use keywords
# for = 1

# rule 4 - do not use symbols except _
# a.b = 11
# a@b = 11
# a!b = 11
# a*b = 11
# a/b = 11

# rule 5 - any length



