"""
flow control - continue
ignore even number
"""
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue

    print(count)
    count += 1


