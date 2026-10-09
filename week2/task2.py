num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    if num1 == num2:
        print(f"The largest numbers are {num1} and {num2}.")
    elif num1 == num3:
        print(f"The largest numbers are {num1} and {num3}.")
    else:
        print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    if num2 == num3:
        print(f"The largest numbers are {num2} and {num3}.")
    else:
        print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")