"""
output formatting
string  format()
named arguments
"""
name1 = 'Obama'
name2 = 'Helen'
name3 = 'Marie'
name4 = "Cindy"

greeting1 = "morning!"
greeting2 = "afternoon!"
greeting3 = "evening!"

print("Good {grt3}, {n3}! Long time no see".format(n3=name3, grt3=greeting3))

print("Good {grt3}, {n3}, {n1} and {n4} ! Long time no see".format(n3=name3, n4=name4, n1=name1, grt3=greeting3))
print("Good {grt3}, {n3}, {n1} and {n4} ! Long time no see".format(grt3=greeting3, n1=name1, n3=name3, n4=name4))