# arbitrary arguments
# get the number of arguments, and print out


def count(*names):
    return len(names)


length = count("Puma", "Alex", "Bill", "Mark", "David")
# length = count("Puma", "Alex", "Bill", "Mark", "David")
# length = count()
print(length)
