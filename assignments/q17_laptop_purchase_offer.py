"""Q17. Laptop Purchase Offer"""

student = input("Are you a student Yes/No: ")
purchase_amount = float(input("Enter purchase amount: "))

if student == "Yes" or student == "yes":
    if purchase_amount > 50000:
        print("Student Discount + Backpack")
    else:
        print("Student Discount")
else:
    if purchase_amount > 70000:
        print("Free Mouse")
    else:
        print("No Offer")
