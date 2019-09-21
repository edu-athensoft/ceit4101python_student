# concatenation

str1 = "ABC"
str2 = "DEF"
str3 = "GHI"

# using +
a = str1+str2+str3
print(a)

# using *
b = str1*3
print(b)

# String Membership Test
print('A' in a)
print('A' not in a)


# format
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

first_name = "Lisa"
last_name = "Regan"
print("Welcome, {} {}! Thank you to use this system!".format(first_name, last_name, "aaa"))
print("Welcome, {} {}! Thank you to use this system!".format(first_name))

