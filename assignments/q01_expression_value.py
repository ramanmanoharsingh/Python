"""Q1. Expression Value"""

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

answer = a ** 2 + b ** 2 + c ** 2 + 2 * (a * b * c) ** 0.5

print("Value of expression:", answer)
