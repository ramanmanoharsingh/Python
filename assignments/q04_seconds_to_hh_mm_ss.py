"""Q4. Seconds to HH:MM:SS"""

seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(hours, ":", minutes, ":", seconds)
