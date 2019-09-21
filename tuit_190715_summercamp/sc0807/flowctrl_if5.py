# input a number of income
income = input("Enter your income for last year: (k/year)")
statement_income= ''
statement_gstqst= ''

# making decision by the gov
income = int(income)

if income <= 22:
    statement_income = '0%'
    statement_gstqst = '100%'
elif income <= 36:
    statement_income = '15%'
    statement_gstqst = '80%'
elif income <= 58:
    statement_income = '33%'
    statement_gstqst = '50%'
elif income <= 100:
    statement_income = '40%'
    statement_gstqst = '25%'
else:
    statement_income = '50%'
    statement_gstqst = '0%'

# output the assessment of notice
print("Your Notice of Assessment from RQ and CRA is:\n")
print("Your income of last year is ${}k \n".format(income))
print("You should pay the income tax by: {}".format(statement_income))
print("You should get the return of GST/QST by: {}".format(statement_gstqst))
