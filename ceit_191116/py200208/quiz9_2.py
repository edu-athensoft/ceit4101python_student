"""
quiz 9-2
"""

num_list = [4,3,2,1,5,7,6,8,9,10]

min = num_list[0]
max = num_list[0]

if num_list[1]>max:
    max = num_list[1]

if num_list[1]<min:
    min = num_list[1]

if num_list[2] > max:
    max = num_list[2]

if num_list[2] < min:
    min = num_list[2]

if num_list[3] > max:
    max = num_list[3]

if num_list[3] < min:
    min = num_list[3]

if num_list[4] > max:
    max = num_list[4]

if num_list[4] < min:
    min = num_list[4]

if num_list[5] > max:
    max = num_list[5]

if num_list[5] < min:
    min = num_list[5]

if num_list[6] > max:
    max = num_list[6]

if num_list[6] < min:
    min = num_list[6]

if num_list[7] > max:
    max = num_list[7]

if num_list[7] < min:
    min = num_list[7]

if num_list[8] > max:
    max = num_list[8]

if num_list[8] < min:
    min = num_list[8]

if num_list[9] > max:
    max = num_list[9]

if num_list[9] < min:
    min = num_list[9]

print(num_list)
print("The max number of the list is {}".format(max))
print("The min number of the list is {}".format(min))