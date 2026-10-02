# Asking for student details
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
department = input("Enter department: ")
year = int(input("Enter year: "))
university = input("Enter university: ")
phone = input("Enter phone number: ")

# Displaying the formatted Student ID Card
print("\n" + "+" + "-" * 32 + "+")
print("|       AKIBA STUDENT CARD       |")
print("+" + "-" * 32 + "+")
print(f"| Name: {name:<24} |")
print(f"| ID: {student_id:<26} |")
print(f"| Department: {department:<18} |")
print(f"| Year: {year:<24} |")
print(f"| University: {university:<18} |")
print(f"| Phone: {phone:<23} |")
print("+" + "-" * 32 + "+")