# Collect student information
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")
city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")
favorite_language = input("Enter your favorite programming language: ")
programming_goal = input("Enter your programming goal: ")

# Display student profile
print("=" * 50)
print("              STUDENT PROFILE")
print("=" * 50)

print(f"{'Name:':<25}{full_name}")
print(f"{'Student ID:':<25}{student_id}")
print(f"{'Age:':<25}{age}")
print(f"{'City:':<25}{city}")
print(f"{'University:':<25}{university}")
print(f"{'Department:':<25}{department}")
print(f"{'Email:':<25}{email}")
print(f"{'Phone:':<25}{phone_number}")
print(f"{'Favorite Language:':<25}{favorite_language}")

print("\nProgramming Goal:")
print(programming_goal)

print("=" * 50)