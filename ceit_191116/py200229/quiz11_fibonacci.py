"""
fibonacci sequence
"""

nterms = int(input("Enter how many terms?"))

n1, n2 = 0, 1
count = 0

if nterms <=0:
    print("please enter a positive number")
elif nterms == 1:
    print(n1)
elif nterms == 2:
    print(n1,n2)
else:
    while count<nterms:
        print(n1, end=",")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
