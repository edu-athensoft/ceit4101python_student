"""
convert list, tuple to dict
"""

list1 = [['a',1, 2],
        ['b',2, 2]
         ]

tuple1 = (('a',1, 2),
          ('b',2, 2)
          )

#
list1 = [['a',2],
        ['b',2]
         ]

tuple1 = (('a',1),
          ('b',1)
          )


# dict -> list
# dict -> tuple

dict1 = dict(list1)
print(dict1)

print(list(dict1))