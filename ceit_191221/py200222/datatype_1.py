"""
datatype
"""
# numeric type
# for variables
num = 10.5
print(num, type(num))

# for values
print(num, type(10.5))
print()


# for string

print()

# for boolean
print()

# for list
print()

# for tuple
print()

# for set
print()

# for dictionary
client_info2 ={
    "ON0001" : [289375237423,'Peter','900108'],
    "QC0001" : (289375237423,'Peter','900108'),
    "QC0002" : [289375237423,'Peter','900108'],
    "QC0003" : [289375237423,'Peter','900108'],
    "QC0004" : [289375237423,'Peter','900108'],
    "SK0003" : [289375237423,'Peter','900108']
}

# output type of dict
print(type(client_info2))

# output type of the key of dict
print(type("ON0001"))

# output type of the value of dict by a specified key
print(type(client_info2["ON0001"]))
print(type(client_info2["QC0001"]))

