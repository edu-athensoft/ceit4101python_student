"""
python output
print()
"""

# case 1
print("literal")

# case 2
a = True
print(a)

# case 3
print("abc", 123, True)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# case 4 - sep=","
print("abc", 123, True, sep=",")

# case 5
print()
print("====")

print("\n")
print("====")

# output to file system
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh aksdfjasdfkadsfasdf askdfjasldfj asf !', file = sourceFile)
sourceFile.close()

