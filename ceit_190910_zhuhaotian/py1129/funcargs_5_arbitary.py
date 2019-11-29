# arbitrary arguments


def count(*names):
    print(type(names))
    for i in names:
        print(i)


count("Puma", "Alex", "Bill", "Mark", "David")
