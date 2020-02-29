"""
flow control - continue
"""
count = 0
while count < 10:
    if count == 6:
        count += 1
        continue

    print(count)
    count += 1


