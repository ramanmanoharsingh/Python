"""Q18. Online Movie Booking System"""

show_time = input("Enter show time Morning/Evening: ")
age_category = input("Enter age category Child/Adult: ")
tickets = int(input("Enter number of tickets: "))
booking_day = input("Enter booking day: ")

ticket_price = 0
discount = 0
convenience_charge = 0

if show_time == "Morning" or show_time == "morning":
    if age_category == "Child" or age_category == "child":
        ticket_price = 120
    elif age_category == "Adult" or age_category == "adult":
        ticket_price = 180
elif show_time == "Evening" or show_time == "evening":
    if age_category == "Child" or age_category == "child":
        ticket_price = 180
    elif age_category == "Adult" or age_category == "adult":
        ticket_price = 250

ticket_cost = ticket_price * tickets

if tickets > 5:
    discount = 10 / 100 * ticket_cost

if booking_day == "Sunday" or booking_day == "sunday":
    convenience_charge = 50

final_amount = ticket_cost - discount + convenience_charge

print("Ticket Cost:", ticket_cost)
print("Discount:", discount)
print("Convenience Charge:", convenience_charge)
print("Final Amount:", final_amount)
