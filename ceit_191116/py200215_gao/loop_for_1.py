"""
for
"""

# case 1
# print out all items of a given list using for-loop

"""
given list is  a = [1,2,3,4,5,6,7]
the result is surposed to be:
  1
  2
  3
  4
  5
  6
  7

step 1:  
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)

step 2:
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

step 3: figure out the pattern of the body of loop
print(a[i])

step 4: construct the loop structure
for i in a:
    print(i)

"""

# case 1
a = [1, 2, 3, 4, 5, 6, 7]
for i in a:
    print(i)

print("===========")

# case 2-1
for i in [1, 2, 3, 4, 5, 6, 7]:
    print(i)


# case 2-2
for i in (1, 2, 3, 4, 5, 6, 7):
    print(i)

# case 2-3
for i in "hello python":
    print(i)

for i in ['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']:
    print(i)
