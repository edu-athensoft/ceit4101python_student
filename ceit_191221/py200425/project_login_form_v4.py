times = 3
count = 0
while  count < times:
    count += 1
    name = input("what is your username")
    password = input("what is your password")

    if name == "Admin":
        if password == "root":
            print("welcome")
            break
        else:
            print("try again")
    else:
        print("try again QAQ")

else:
    ("your acount is blocked")