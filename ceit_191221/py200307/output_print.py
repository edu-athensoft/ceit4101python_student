"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""

# case 1
a = 1.09
print(a)

print(1.09)

print(a, '1.09')
print(a, '1.09', a, '1.09')

# sep
print(a, '1.09', a, '1.09', sep='; ')

# end
print()     # empty line
print()
print("adsfjlkasdlfadsf", end="\t")
print("adsfjlkasdlfadsf", end="\t")
print("============")

a = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
print(a[0],end="\t")
print(a[1],end="\t")
print(a[2],end="\t")
print(a[3],end="\t")


# file
myfile = open("mydata.txt", 'w')
print(a, file=myfile)
myfile.close()




