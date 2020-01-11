"""
import external modules or libraries
"""

# import ceit_191116.py200111.myconst
#
# print(ceit_191116.py200111.myconst.PI)

import ceit_191116.py200111.myconst as myconst

print(myconst.PI)
print(myconst.G)

import sys
print(sys.path)

import math
print(math.sin(myconst.PI/2))