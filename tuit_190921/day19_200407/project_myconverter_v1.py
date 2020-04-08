"""
project:    my simple converter
version:    1.0
date:       2020-04-07
author:     Athens

"""

"""
Objectives:	Using python programming skills to model and solve problem

Version:	1
Iteration plan:	build up the project implementing basic business logic or function

Directions:	
You are asked to write an application of a unit converter in Python. It is a text-based UI (user interface).  The application has a menu system of two levels as the following. 

Users can Input a valid number, and get the result of converted value with necessary text descriptions from the system console.


Menu level 1 - Choose a converter type
1. Length or distance
2. Temperature
3. Weight or mass
4. Area
(4 classes)

Menu level 2 - Choose a converting method
1.1 kilometers to miles
1.2 miles to kilometers
(3-4 sets/pairs)

"""


"""
Plan
1. Menu System
  1.1 Top-level (1st level)
       prompt (show in one line, show at multiple lines)
       input top level num
       show the num at console
  1.2 Second-level (2nd level)
        prompt
        input
        based on the input of 1st level
"""


# choose at 1st level
level_1 = input("Please choose a measure class:\n1. Length\n2. Mass\n3. Temperature\n4. Volume")
print("you chose {}".format(level_1))

# choose at 2nd level









