"""
conversion between for loop and while loop
"""
print("=== for loop ===")
for i in range(10):
    print("hello-for")


print("=== while loop ===")
i = 0
N = 10
# 11 is N+1 where N = 10
while i < N:
    print("hello-while")
    i += 1
