sym = input("Enter a string: ")
size = int(input("Enter arrow's size (greater than 0): "))

if size % 2 == 0:
    for i in range(size // 2):
        print(" " * i + sym)
    for i in range(size // 2):
        print(" " * (size // 2 - i - 1) + sym)
else:
    for i in range(size // 2 + 1):
        print(" " * i + sym)
    for i in range(size // 2):
        print(" " * (size // 2 - i - 1) + sym)
if size == 0:
    print("Size must be greater than 0.")
