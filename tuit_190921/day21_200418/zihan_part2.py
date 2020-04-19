def check_if_valid(i):
    no_of_times = 0
    for i in input_list:
        if i == input_character:
            no_of_times += 1
    return no_of_times

input_list = list(input("Please input a string:     "))
input_character = str(input("Please input a character:      "))
no_of_times = 0
valid_times = no_of_times
print(valid_times)