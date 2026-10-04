
# Collect user information
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI report
print("=" * 35)
print("           BMI REPORT")
print("=" * 35)

print(f"Name:   {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height:.2f} m")

print("-" * 35)
print(f"BMI:    {bmi:.2f}")
print("=" * 35)
