rows, cols = list(map(int, input("City Size: ").split()))
grid = []

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)


def view(grid):
    views = 0
    m, n = len(grid), len(grid[0])
    for i in range(n):
        max = grid[0][i]
        views += 1
        for j in range(1, m):
            if grid[j][i] > max:
                max = grid[j][i]
                views += 1
    return views


def createMatrix(cols, rows):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for _ in range(cols):
            matrix[i].append(0)
    return matrix


def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    transposed = createMatrix(m, n)
    for i in range(n):
        for j in range(m):
            transposed[i][j] = matrix[j][i]
    return transposed


north = grid.copy()
south = list(reversed(grid.copy()))
west = transpose(grid.copy())
east = list(reversed(west.copy()))


views = [("N", view(north)), ("S", view(south)), ("E", view(east)), ("W", view(west))]
max_view = max(views, key=lambda x: x[1])

max_views = [x[0] for x in views if x[1] == max_view[1]]

print(" ".join(max_views))
