# indentation

# correct but not recommened
for i in range(1,11):
  print()
  print()
  for i in range(1,11):
    print(i)
    if i == 5:
      print(int(i))
    if i == 5:
      break

# correct and recommened
# using tab
for i in range(1,11):
    print()
    print()
    for i in range(1, 11):
        print(i)
        if i == 5:
            print(int(i))
        if i == 5:
            break
