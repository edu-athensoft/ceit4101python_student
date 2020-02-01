"""
datatype list
"""

# quarter 1, 2020
balance_q1 = [50, 20, 40]
print(balance_q1[0])
print(balance_q1[1])
print(balance_q1[2])

# quarter 2, 2020
balance_q2 = [60, 70, 80]
print(balance_q2[0])
print(balance_q2[1])
print(balance_q2[2])


# balance of the year of 2020
balance = [ [50, 20, 40],
            [60, 70, 80],
            [60, 70, 80],
            [60, 70, 80]]

balance = [ [50, 20, 40],[60, 70, 80],[60, 70, 80],[60, 70, 80] ]
print(balance)
print(balance[3][2])

balance[3][2] = 90
print(balance)

