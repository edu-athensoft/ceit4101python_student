"""
flow control - break
"""

for i in range(10):
    print(i)
    if i>5:
        break

print("======")

for i in range(10):
    if i>5:
        break
    print(i)

