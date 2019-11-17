# range

# case 1

r = range(0,10);
print(r, type(r))

# case 2
r = list(range(0,10))
print(r, type(r))


# generating a list from 1 to 10
r = list(range(1,11))
print(r)

# range(a)
r = list(range(10))
print(r)

# traversal list using range()
genre = ['pop','jazz','rock']
for i in range(len(genre)):
    print(genre[i])

# range(a,b,c)
r = list(range(1,11,4))
print(r)

