"""Q2. Simple Interest"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
