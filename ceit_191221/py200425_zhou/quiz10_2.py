"""

"""

prod = 1
for i in range(1,21):
    if i%2 == 0:
        prod *= i
print("prod = ",prod)


prod = 1
# 1x2x4x6x8x10x12x…..x20
# 2x4x6x....x20
# 2(1x2x3x..x10)
for i in range(1,11):
    prod *= 2*i
print("prod = ",prod)


prod = 1
for i in range(2,21,2):
    prod *= i
print("prod = ",prod)
