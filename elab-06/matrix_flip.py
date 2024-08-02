direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))

matrix = []
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)


print("After flip:")
if direction == "V":
    matrix.reverse()
    for x in matrix:
        print(" ".join(list(map(str, x))))
else:
    for i in range(size):
        matrix[i].reverse()
    for x in matrix:
        print(" ".join(list(map(str, x))))
