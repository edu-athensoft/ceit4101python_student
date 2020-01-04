"""
python output
"""

# simple output
print()

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *objects
print(1,2,3,4)

# separator by default ' '
print(1,2,3,4,sep=';')

# end by default '\n'
print()
print(1,2,3,4,end="&&")
print(1,2,3,4,end="&&")
print(1,2,3,4)
print(1,2,3,4)

# file output by default sys.stdout

# flush = False|True

