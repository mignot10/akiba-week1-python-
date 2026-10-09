pin = 1234
count = 0

while count < 3:
    pass_key = int(input("Enter PIN: "))
    count += 1
    if pass_key == pin: 
        print("correct pin go ahead")
        break
    else: 
        if count == 3: print("Try after 60min")
        else: 
            print("Incorrect PIN")
            print("Attemps remaining: ", 3 - count )
            