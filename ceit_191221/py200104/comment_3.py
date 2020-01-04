

# adsfasdfas

# a = 1

"""
comment
docstring
as the first statement of a module
"""


def my_balance(year, month):
    '''
    to calculate client's balance on monthly basis
    :param year: specified year - yyyy
    :param month: specified month - mm
    :return: the balance of the specified year and month
    '''
    balance = 1000
    print()
    print("Year : " + str(year))
    print("Month :" , month)
    print("The balance is:" , balance)
    return balance


year = 2020
print(year)
print("Year is :", 2020)    # yyyy
print("Month is :", "JAN")  # MMM
print("The Balance is :", 305000.00)

# use docstring of the function
print(my_balance.__doc__)