import random

number = random.randint(1,10)
count = 0

while count < 5:
    guess = int(input("Guess the number, you have 5 chances: "))
    count += 1

    if guess == number: 
        print(f"Congratulations! you guessed the number in {count} attempts ")
        break
    else: 
        if count == 5: 
            print("Game over")
            print(f"The secret number was {number}")
        else: print("you have ", 5 - count , "attempts left.")
        
