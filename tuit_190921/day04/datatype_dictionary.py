# dictionary is an unordered collection
# dictionary is a collection of key-value pairs

my_dict1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

my_dict2 = {
    "MON": "Monday",
    "TUE": "Tuesday",
    "WED": "Wednesday",
    "THU": "Thursday",
    "FRI": "Friday",
    "SAT": "Saturday",
    "SUN": "Sunday"
}

print(my_dict2, type(my_dict2))
print(my_dict2['MON'])
# print(my_dict2['Monday'])
print(my_dict2["SAT"])
print(my_dict2["SUN"])

my_dict3 = {
    1: "Gold",
    2: "Silver",
    3: "Bronze"
}
print(my_dict3[1])
print(my_dict3[2])
print(my_dict3[3])
print(my_dict3[1],my_dict3[2],my_dict3[3])

