"""
to use constants from external file
"""

# alias
import tuit_200302.py200306.myconst as myconst

# to calculate G = mg
m = 1.0 # mass, 1.0 kg
g = myconst.GRAVITY
G = m*g
print("The gravity of the object (mass={}) is {}. ".format(m,G))


# to calculate the area of a circle where the radius is 10
# S = PI*r^2

r = 10
area = myconst.PI * r * r
print("The area of the circle with the radius=10 is {}".format(area))

