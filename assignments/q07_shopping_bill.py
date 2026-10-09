"""Q7. Shopping Bill"""

total_amount = float(input("Enter total amount: "))

discount = 10 / 100 * total_amount
gst = 18 / 100 * (total_amount - discount)

final_bill = total_amount - discount + gst

print("Discount:", discount)
print("GST:", gst)
print("Final Bill:", final_bill)
