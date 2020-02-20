"""
literal collections
"""

# List
my_list = [1,2,3,4,5,6]
my_list = ['a','bb','cc','dd']
my_list = ['a',34,"lkdsjfkdsa",True, 1.25]

# Tuple
my_tuple = (1,2,3,4,5,6)
my_tuple = ('a','bb','cc','dd')
my_tuple = ('a',34,"lkdsjfkdsa",True, 1.25)

# Set
my_set = {1,2,3,'ab',True}

# Dictionary
# collection of key-value pairs
my_db_conn = {
    "ConnectionName": "remote-mysql8",
    "Host": "156.23.46.233",
    "Port": 3306,
    "User": "root",
    "Password": "123abc"
}
print(my_db_conn)