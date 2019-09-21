# for val in sequence:
# 	Body of for

subtotal = 0
GST_RATE = 0.05
QST_RATE = 0.09975
gst_amount = 0.0
qst_amount = 0.0
item_list = [650, 15, 24, 56, 280]

for item_amount in item_list:
    subtotal = subtotal + item_amount
    # to write your code below for GST
    gst_amount = gst_amount + item_amount * GST_RATE
    # to write your code below for QST
    qst_amount = qst_amount + item_amount * QST_RATE

print("The subtotal of {} is {}".format(item_list, subtotal))
print("The GST of {} is {}".format(item_list, gst_amount))
print("The QST of {} is {}".format(item_list, qst_amount))

grand_total = subtotal+gst_amount+qst_amount
print("The grand total".format(grand_total))