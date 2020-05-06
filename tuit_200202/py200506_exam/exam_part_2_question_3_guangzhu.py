"""
my idea is to use a function, then put things in the function and print out with another loop which i put
a variable already set connected to the function.
"""

def randomizer(x):
   if len(x) == 0:
      return []
   if len(x) == 1:
      return [x]
   b = []
   for i in range(len(x)):
      c = x[i]
      a = x[:i] + x[i + 1:]
      for y in randomizer(a):
         b.append([c] + y)
   return b
z = list(input('Please enter a string:'))
set(z)
for y in randomizer(z):
   print(y)

