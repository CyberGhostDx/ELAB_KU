cols, rows = list(map(int, input("Grid Size: ").split()))
m = int(input("Number of mine(s): "))


def createGrid(cols, rows):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(0)
    return grid


grid = createGrid(cols, rows)

for i in range(m):
    y, x = list(map(int, input(f"Mine#{i+1}: ").split()))
    grid[x][y] = "X"

check_index = [-1, 0, 1]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] != "X":
            for c in check_index:
                for r in check_index:
                    if i + r < rows and j + c < cols:
                        if grid[i + r][j + c] == "X" and i + r >= 0 and j + c >= 0:
                            grid[i][j] += 1

for i in grid:
    print(" ".join(map(str, i)))
