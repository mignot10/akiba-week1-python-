# Collect employee information
employee_name = input("Enter employee name: ")

# Collect salary details
basic_salary = float(input("Enter basic salary (ETB): "))
transport_allowance = float(input("Enter transport allowance (ETB): "))
food_allowance = float(input("Enter food allowance (ETB): "))

# Calculate gross salary
gross_salary = basic_salary + transport_allowance + food_allowance

# Display employee payslip
print("=" * 45)
print("              EMPLOYEE PAYSLIP")
print("=" * 45)

print(f"Employee: {employee_name}")
print()
print(f"{'Basic Salary:':<25}{basic_salary:>15,.2f} ETB")
print(f"{'Transport Allowance:':<25}{transport_allowance:>15,.2f} ETB")
print(f"{'Food Allowance:':<25}{food_allowance:>15,.2f} ETB")

print("-" * 45)
print(f"{'Gross Salary:':<25}{gross_salary:>15,.2f} ETB")
print("=" * 45)
