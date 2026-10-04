#collect travel information
destination = input("Enter the destination: ");
distance = float(input("Enter the distance in km: "));
speedAvg = float(input("Enter the average speed in km/h: "));

# Calculate travel time
time = distance / speedAvg;

hour = int(time);
minute = int((time - hour) * 60);

# Display travel time report
print ("\n" + "=" * 40)
print("        TRAVEL TIME CALCULATOR")
print("=" * 40)
print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speedAvg} km/h")
print(f"Estimated Time: {hour} hours and {minute} minutes")
