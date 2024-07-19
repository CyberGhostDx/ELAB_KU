n = int(input("secret number = "))

for i in range(3):
    g = int(input("Enter your guess : "))
    if g != n and i == 2:
        print("You've used all your attempts.")
        break
    if g > n:
        print("Sorry, your guess is too high, pls try again.")
    elif g < n:
        print("Sorry, your guess is too low, pls try again.")
    elif g == n:
        print("Congratulations, your guess is correct.")
        break
