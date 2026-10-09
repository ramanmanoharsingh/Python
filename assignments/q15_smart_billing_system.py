"""Q15. Smart Billing System"""

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

if bill > 2000:
    bill = bill - 200

print("Final Bill:", bill)
