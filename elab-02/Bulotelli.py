is_injure = input("Is Bulotelli injured?(y/n) ")

if (is_injure == "n"):
    is_late = input("Is Bulotelli late for the training?(y/n) ")
    if (is_late == "y"):
        is_well = input("Did Bulotelli perform well in training?(y/n) ")
        if is_well == "y":
            print("Substitute")
        elif is_well == "n":
            print("Not selected")
    elif (is_late == "n"):
        print("Starter")

elif (is_injure == "y"):
    print("Not available")
