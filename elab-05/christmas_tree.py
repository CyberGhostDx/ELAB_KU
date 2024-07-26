bush = int(input("How many bushes? "))
size = int(input("Enter bush size: "))

for _ in range(bush):
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
