# input

my_list = []

while True:
    a = input("Enter a number: ")
    if a == 'exit':
        break;
    else:
        a = float(a)
        my_list.append(a)

print(my_list)

# calculate the summary
summary = 0
for item in my_list:
    summary = summary + item

# output
print("this sum of your input of {} is {}".format(my_list, summary))