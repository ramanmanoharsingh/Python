"""Q10. Traffic Light Simulator"""

color = input("Enter traffic light color: ")

if color == "Red" or color == "red":
    print("Stop")
elif color == "Yellow" or color == "yellow":
    print("Get Ready")
elif color == "Green" or color == "green":
    print("Go")
else:
    print("Invalid Signal")
