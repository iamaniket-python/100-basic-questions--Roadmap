# Write a program to read seconds and convert them into hours, minutes and seconds

seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

# Enter total seconds: 98
# Hours: 0
# Minutes: 1
# Seconds: 38