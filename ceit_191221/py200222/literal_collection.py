"""
literal collections
"""

"""
collections
    List
    Tuple
    Set
    Dictionary
"""

# list literal
# unit k dollars
balance_by_quarter_2019 = [110, 120, 130, 140]
salary_it_dev = [65, 70, 80, 100]
# QC, ON, BC, US
# angler bracket, braces
# mutable


# tuple literal
balance_by_quarter_2019 = (10, 120, 130, 140)
salary_it_dev = (65, 70, 80, 100)
# parenthesis  ()
# coordinates
# protective purpose, security purpose
# immutable


# set literal
day_of_week = {'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'}
season = {'SPRING', 'SUMMER', 'FALL', 'WINTER'}
# curly braces
print(season)

# eliminate duplicates
season = {'SPRING', 'SUMMER', 'FALL', 'WINTER', 'SPRING', 'SPRING'}
print(season)


# dictionary literal
# scenario #1
server_config = {
    "connectionName": "Financial DB",
    "Host": "192.168.1.200",
    "HostName": "finance.dc.abc.com",
    "port": 3306,
    "userName": "director",
    "password": "pwd2020"
}

# client info
client_info ={
    "ON0001" : 289375237423,
    "QC0001" : 434853456056,
    "QC0002" : 434858886056,
    "QC0003" : 434853456056,
    "QC0004" : 434899956056,
    "SK0003" : 958594695485
}

client_info2 ={
    "ON0001" : [289375237423,'Peter','900108'],
    "QC0001" : [289375237423,'Peter','900108'],
    "QC0002" : [289375237423,'Peter','900108'],
    "QC0003" : [289375237423,'Peter','900108'],
    "QC0004" : [289375237423,'Peter','900108'],
    "SK0003" : [289375237423,'Peter','900108']
}

print(client_info2['QC0001'])








