"""
loop continue
"""

for i in range(10):
    print(i, end="\t")
    if i == 6:
        continue

print()

for i in range(10):
    if i == 6:
        continue
    print(i, end="\t")
