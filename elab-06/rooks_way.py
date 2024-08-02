row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))

for i in range(8):
    print("-----------------")
    for j in range(8):
        if j == col and i == row:
            print("|R", end="")
            continue
        elif j == col or i == row:
            print("|x", end="")
            continue
        print("| ", end="")
    print("|")


print("-----------------")
