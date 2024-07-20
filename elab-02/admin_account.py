u = input("Username: ")
p = input("Password: ")

if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
    print("Welcome, admin.")
else:
    print("You are not admin.")
