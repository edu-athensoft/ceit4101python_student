# datatype dictionary

# declaring a dict
dict1 = {
    101: 'Peter',
    102: 'White',
    201: 'Lisa',
    202: 'Mary',
    301: 'Bill',
    302: 'Isabel'
}
print(dict1)
print(type(dict1))

dict2 = {
    '101': 'Peter',
    102: 'White',
    '201': 'Lisa',
    202: 'Mary',
    '301': 'Bill',
    302: 'Isabel'
}
print(dict2['101'])
print(dict2[102])
