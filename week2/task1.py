#ask for input 
number = float(input("Enter a number: "))

#check even or odd
if ( number % 2 == 0):
    if ( number > 0):
        print(" positive even number.")
    elif ( number < 0 ):
        print("Negative even number")
    else: 
        print("Zero (even number)")
else:
    if number > 0:
        print("positive odd number")
    else: 
        print("negative odd number")
