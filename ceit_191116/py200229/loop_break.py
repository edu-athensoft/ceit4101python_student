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


# ==============

#
print("=== nested for loop ===")
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(i,j)

