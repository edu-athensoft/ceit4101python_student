"""
datatype
dictionary
"""

# create a dictionary
IP_ADDRESS = "192.168.1.12"
PORT = 3306

my_dict = {
    "IP": IP_ADDRESS,
    "PORT": PORT
}

print(my_dict)
print("http://"+my_dict["IP"]+":"+str(my_dict["PORT"]))



