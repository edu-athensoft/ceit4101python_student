invoice = [
    "{:70}{:>10}".format("East Repair Inc.","INVOICE"), #80
    "{}".format("1912 Harvest Lane New York"),
    "{}".format("NY 12210"),
    "{:20}{:20}{:>20}{:>20}".format("Bill To","Ship To","Invoice#","US-001"),
    "{:20}{:20}{:>20}{:>20}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"),
    "{:20}{:20}{:>20}{:>20}".format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"),
    "{:20}{:20}{:>20}{:>20}".format("New York,NY 12210", "Cambridge,MA 12210", "Due Date", "26/02/2019")
]

farbc = 100.00
nsopa = 30.00
l3 = 15.00
sales_tax = 6.25

entriers = [
    "|{:^5}|{:^35}|{:^15}|{:^25}|".format("QTY", "DESCRIPTION ", "UNIT PRICE", "AMOUNT"),
    "|{:^5}|{:35}|{:>15}|{:>25.2f}|".format("1", "Front and rear brake cables", "100.00", farbc),
    "|{:^5}|{:35}|{:>15}|{:>25.2f}|".format("2", "New set of pedal arms", "15.00", nsopa),
    "|{:^5}|{:35}|{:>15}|{:>25.2f}|".format("3", "Labor 3hrs", "5.00", l3),
    " {:^5} {:35} {:>15} {:>25.2f}".format("", "", "Subtotal", farbc+nsopa+l3),
    " {:^5} {:^35} {:>15} {:>25.2f}".format("", "", "Sales Tax 6.25%", (farbc+nsopa+l3)*0.0625),
    " {:^5} {:^35} {:>15} {:>25.2f}".format("", "", "TOTAL", (farbc+nsopa+l3)*1.0625)

]

footer = [
    "{:80}".format("Terms & Conditions"),
    "{:80}".format("Payment us due within 15 days"),
    "{:80}".format(""),
    "{:80}".format("Please make checks payable to:East Repair Inc.")
]



print(invoice[0])
print(invoice[1])
print(invoice[2])
print(invoice[3])
print(invoice[4])
print(invoice[5])
print(invoice[6])
print(entriers[0])
print(entriers[1])
print(entriers[2])
print(entriers[3])
print(entriers[4])
print(entriers[5])
print(entriers[6])
print(footer[0])
print(footer[1])
print(footer[2])
print(footer[3])
