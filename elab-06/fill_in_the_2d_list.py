size = int(input("Enter the number of rows or columns : "))

for i in range(size):
    for j in range(i + 1, size + i + 1):
        print(f"%2d" % j, end=" ")
    print()
