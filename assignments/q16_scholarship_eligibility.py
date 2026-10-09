"""Q16. Scholarship Eligibility"""

student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))
family_income = float(input("Enter family income: "))
sports_quota = input("Sports quota Yes/No: ")

scholarship_type = "No scholarship"
scholarship_amount = 0
extra_support = 0

if marks >= 90:
    scholarship_type = "Full scholarship"
    scholarship_amount = 50000
elif marks >= 75 and marks <= 89:
    if family_income < 300000:
        scholarship_type = "Half scholarship"
        scholarship_amount = 25000
    else:
        scholarship_type = "No scholarship"
        scholarship_amount = 0
else:
    scholarship_type = "No scholarship"
    scholarship_amount = 0

if sports_quota == "Yes" or sports_quota == "yes":
    extra_support = 5000

print("Student Name:", student_name)
print("Scholarship Type:", scholarship_type)
print("Scholarship Amount:", scholarship_amount)
print("Extra Support Amount:", extra_support)
