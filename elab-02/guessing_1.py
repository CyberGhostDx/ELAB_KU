number = float(input("Enter your guess (0 - 100): "))

if number > 100 or number < 0:
    print("Sorry, out of range, try again later.")
elif number == target:
    print("Congratulations, your guess is correct.")
elif number != target:
    print("Sorry, your guess is wrong, try again later.")
