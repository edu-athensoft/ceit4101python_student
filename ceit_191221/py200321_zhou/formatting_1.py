"""
string output formatting

syntax
template.format(p0, p1, ..., k0=v0, k1=v1, ...)
"""

name = "Athensoft"
corp = "Inc."
date = '2020-03-21'
time = '14:00'
print('{} and {} --- {nm} is {corp}'.format(date, time, nm = name, corp=corp))

# print('{nm} is {corp} --- {} and {}'.format(nm = name, corp=corp, date, time )) #error
# print('{nm} is {corp} --- {2} and {3}'.format(nm = name, corp=corp, date, time )) #error
