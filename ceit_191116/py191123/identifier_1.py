# test rule 1

# valid identifier
abc = 888
abc123 = 888
abc123_ = 888
_123 = 888

# invalid id
# $ddd = 999
# ddd-ff = 999
# dd ff= 99

# test rule 2
_123 = 88
__abc__ = 88
# 99abc = 888
# 9_ = 888

# test rule 3 keywords

# test rule 4 refer to rule 1

# special identifier
class myclass:
    __doc__ = 'aaa'
    doc = "aaa"

print(myclass.__doc__)
print(myclass.doc)





