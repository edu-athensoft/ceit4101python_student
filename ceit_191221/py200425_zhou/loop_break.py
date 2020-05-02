"""
loop break
"""

for i in range(10):
    print(i)

print()


for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("exit")


print()

for i in range(10):
    if i == 5:
        break
    print(i)
