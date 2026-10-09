numbers = list(map(int, input("Enter 10 numbers separated by spaces: ").split()))

total = 0
even = 0
odd = 0

for i in range(len(numbers)):
    number = numbers[i]

    total += number

    if i == 0: 
        largest = number
        smallest = number 
    else: 
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    if number % 2 == 0:
            even += 1
    else:
         odd += 1

    
average = total / len(numbers)

print("Largest number:", largest) 
print("Smallest number:", smallest) 
print("Total sum:", total) 
print("Average:", average)
print("Even numbers:", even)
print("Odd numbers:", odd)