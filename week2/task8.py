number = int(input("enter the number: "))

number = abs(number)
even = 0
odd = 0
sum = 0
i= 0
while i < number:
    sum  += i
    if i % 2 == 0: even += 1
    else: odd += 1

    i += 1
    
print(f"we have {even} even numbers and {odd} numbers")
print(f"the sum of all numbers: {sum} ")
