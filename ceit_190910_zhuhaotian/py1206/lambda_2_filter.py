#

my_list = [1,3,4,5,6,16,63,3,14,3,5,89]

for i in my_list:
    print(i)

print("==========")

for i in my_list:
    if i%2 ==0:
        print(i)

# using lambda function
new_list = list(filter(lambda x: x%2==0 ,my_list))
print(new_list)

a = filter(lambda x: x%2==0 ,my_list)
print(a, type(a))

