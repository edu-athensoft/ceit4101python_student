"""
project invoice v2
"""

item0 = [1, "Gaming desktop", 1000.00]
item0.append(item0[0]*item0[2])

item1 = [2, "Keyboard Razor", 150.00]
item1.append(item1[0]*item1[2])

item2 = [30, "Spring Water", 2.00]
item2.append(item2[0]*item2[2])

items = [item0,item1,item2]

# print(items)
# item header
item_template_header = "|{:^5}|{:^45}|{:^15}|{:^15}|"
item_header = item_template_header.format("QTY", "DESCRIPTION ", "UNIT PRICE", "AMOUNT")

# item data
item_template = "|{:^5}|{:45}|{:>15}|{:>15}|"
line = "{:-<85s}".format("")
entries = [
line,
    item_header,
line,
    item_template.format(items[0][0],items[0][1],items[0][2],items[0][3]),
line,
    item_template.format(items[1][0],items[1][1],items[1][2],items[1][3]),
line,
    item_template.format(items[2][0],items[2][1],items[2][2],items[2][3]),
line,
]

print(entries[0])
print(entries[1])
print(entries[2])
print(entries[3])
print(entries[4])
print(entries[5])
print(entries[6])
print(entries[7])
print(entries[8])


subtotal = items[0][3]+items[1][3]+items[2][3]
TAX_RATE = 0.0625
tax = subtotal * TAX_RATE
total = subtotal + tax
summary_template = " {:^5} {:45}|{:>15}| {:>14.2f}|"
summaries = [
    summary_template.format("", "", "Subtotal", subtotal),
    summary_template.format("", "", "Sales Tax 6.25%", tax),
    summary_template.format("", "", "TOTAL", total)
]

print(summaries[0])
print(summaries[1])
print(summaries[2])

