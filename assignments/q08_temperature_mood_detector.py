"""Q8. Temperature Mood Detector"""

temperature = float(input("Enter temperature: "))

if temperature > 35:
    print("It's too hot! Drink water")
elif temperature >= 20 and temperature <= 35:
    print("Nice weather!")
else:
    print("It's cold! Wear a jacket")
