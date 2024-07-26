n = int(input())

area = []

for i in range(n):
    area.append(list(input()))

width = n
height = n
kill = 0

check_index = [-2, -1, 0, 1, 2]

for i in range(width):
    for j in range(height):
        if area[i][j] == "G":
            for c in check_index:
                for r in check_index:
                    if i + c < width and j + r < height:
                        if area[i + c][j + r] == "E" and i + c >= 0 and j + r >= 0:
                            area[i + c][j + r] = "."
                            kill += 1

print(kill)
