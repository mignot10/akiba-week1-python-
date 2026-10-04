# collect student information
name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Mathematics score: "))

# Calculate average
average = (python_score + english_score + math_score) / 3

# Display student result report
print("=" * 40)
print("          STUDENT RESULT")
print("=" * 40)

print(f"Student:      {name}")
print(f"Python:       {python_score}")
print(f"English:      {english_score}")
print(f"Mathematics:  {math_score}")

print("-" * 40)
print(f"Average:      {average:.2f}")
print("=" * 40)
