correct_password = "I love Python"
for i in range(3):
    password = input("Enter password please: ")
    if password != correct_password:
        print(f"Incorrect password, attempt #{i+1}")
        print("Access denied")
    else:
        print("Correct password")
        print("Access granted")
        break
else:
    print("Maximum attempts exceeded")
