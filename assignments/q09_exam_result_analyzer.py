"""Q9. Exam Result Analyzer"""

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 70 and marks <= 89:
    print("Good")
elif marks >= 40 and marks <= 69:
    print("Pass")
else:
    print("Fail")
