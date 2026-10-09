"""Q13. Triangle Type"""

side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
    print("Invalid triangle")
elif side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
