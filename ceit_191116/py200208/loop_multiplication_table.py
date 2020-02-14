"""
multiplication table
12 X 1 to 12 X 10
"""

A = 10
START_NUM = 1
STOP_NUM = 10 + 1

for i in range(START_NUM,STOP_NUM):
    # print("{} x {:2} + tax = {:6.2f}".format(A, i, A*i*1.149975))
    print("{} x {:2} + tax = {:3}".format(A, i, A*i))
