"""
usd to cad
"""


exchange_rate_desc = "1 United States Dollar equals 1.30 Canadian Dollar"
exchange_rate_date = "Jan. 4, 9:17 p.m. UTC · Disclaimer"
RATE_USD_CAD = 1.30

print(exchange_rate_desc)
print(exchange_rate_date)
print()

# input
usd_amount = input("Input the amount of USD:")

# processing
cad_amount = float(usd_amount) * RATE_USD_CAD

# output
print("Exchange rate of USD to CAD is", RATE_USD_CAD)
print("USD$",usd_amount,"equals to", "CAD$", cad_amount)
