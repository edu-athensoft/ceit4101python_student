# format() by index
str1 = 'John'
str2 = 'Bill'
str3 = 'Sean'
positional_order = "{0}, {1} and {2}".format(str1, str2, str3)
print(positional_order)

positional_order = "{1}, {0} and {2}".format(str1, str2, str3)
print(positional_order)


# format() by keyword
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(keyword_order)
