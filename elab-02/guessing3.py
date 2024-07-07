number = float(input("Enter your guess (0 - 100): "))

while 1:
    if number > 100 or number < 0:
        print("Sorry, out of range, try again later.")
    elif number == target:
        print("Congratulations, your guess is correct.")
        break
    elif number != target:
        if(number > target):
            print("Sorry, your guess is too high, try again later.")
        else:
            print("Sorry, your guess is too low, try again later.")
    number = float(input("Enter your guess (0 - 100): "))
