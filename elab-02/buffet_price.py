food_type = ["Korean", "Japanese"]
choice = input("Enter your buffet choice: ")

if choice in food_type:
    is_wed = input("Is today Wednesday (yes/no)? ")
    if is_wed == "yes":
        if (choice == "Korean"):
            print("Your payment is 1275.00 Baht.")
        elif (choice == "Japanese"):
            print("Your payment is 850.00 Baht.")
    elif is_wed == "no":
        if (choice == "Korean"):
            print("Your payment is 1500.00 Baht.")
        elif (choice == "Japanese"):
            print("Your payment is 1000.00 Baht.")
else:
    print(f"Sorry, there is no {choice} buffet.")
