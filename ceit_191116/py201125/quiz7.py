"""
string format()
output an invoice
"""

# analyze data
title = ("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT")
item_1= (1,"Front and rear brake cables",100.0,100.0)
item_2= (2,"New se of pedal arms",15.0, 30.0)
item_3= (3,"Labor 3hrs",5.0,15.0)

subtotal = ("Subtotal", 145.0)
tax = ("Sales Tax 6.25%", 9.06)
total = ("TOTAL", 154.06)

# construct string template
tmplt_title= "{0:^5s} {1:^35s} {2:^18s} {3:^10s}"
print(tmplt_title.format(title[0],title[1],title[2],title[3]))

tmplt_item = "{0:^5d} {1:<35s} {2:>18.2f} {3:>10.2f}"
print(tmplt_item.format(item_1[0],item_1[1],item_1[2],item_1[3]))
print(tmplt_item.format(item_2[0],item_2[1],item_2[2],item_2[3]))
print(tmplt_item.format(item_3[0],item_3[1],item_3[2],item_3[3]))

tmplt_summary= "{0:^5s} {1:<35s} {2:>18s} {3:>10.2f}"
print(tmplt_summary.format("","",subtotal[0],subtotal[1]))
print(tmplt_summary.format("","",tax[0],tax[1]))
print(tmplt_summary.format("","",total[0],total[1]))