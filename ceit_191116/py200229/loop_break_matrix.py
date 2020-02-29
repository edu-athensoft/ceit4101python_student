"""
break from nested loop
4 by 4
"""

matrix = [[11,12,13,14],
        [21,22,23,24],
        [31,32,33,34],
        [41,42,43,44]]
print(matrix)

for i in matrix:
    # print(i)
    for j in i:
        print(j)


# test if break can jump out of the most outer loop
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == 2:
            break
        print(matrix[i][j], end="\t")
    print()

