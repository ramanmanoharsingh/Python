"""Q12. Leap Year and Century Year"""

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")
