"""Q6. Salary Calculation"""

basic_salary = float(input("Enter basic salary: "))

hra = 15 / 100 * basic_salary
da = 50 / 100 * basic_salary
epf = 12 / 100 * (basic_salary + da)

total_salary = basic_salary + hra + da - epf

print("HRA:", hra)
print("DA:", da)
print("EPF:", epf)
print("Total Salary:", total_salary)
