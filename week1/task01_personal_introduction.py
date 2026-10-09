#ask 
name = input("Enter your name: ")
age = int(input("enter your age: "))
city = input("enter your city: ")
university = input("enter your university: ")
department = input("enter your department: ")
favorite_PL = input("enter your favorite programming language: ")
pGoal = input("enter your programming goal: ")


print("\n" + "=" * 40)
print("        STUDENT INTRODUCTION")
print("=" * 40 + "\n")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I study {department} at {university}.")
print(f"My favorite programming language is {favorite_PL}.\n")

print("My programming goal:")
print(f"{pGoal}\n")

print("=" * 40)