def readMat(fn="gauss01.txt"):
    m = []
    with open(fn) as fp:
        for line in fp:
            m.append(line.strip().split(" "))
    return m


def printMat(m):
    for i in range(len(m)):
        row = ""
        for j in range(len(m[0])):
            row += f"{m[i][j]:>8}"
        print(row)
    print()


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.num = numerator // gcd(numerator, denominator)
        self.deno = denominator // gcd(numerator, denominator)
        if self.deno < 0:
            self.num *= -1
            self.deno *= -1

    def evaluate(self) -> float:
        return self.num / self.deno

    def flip(self):
        if self.num < 0:
            self.num *= -1
            self.deno *= -1
        return Fraction(self.deno, self.num)

    def __sub__(self, other) -> "Fraction":
        if isinstance(other, Fraction):
            num = self.num * other.deno
            other_num = other.num * self.deno
            deno = self.deno * other.deno
            return Fraction(num - other_num, deno)
        return Fraction(self.num - other * self.deno, self.deno)

    def __mul__(self, other) -> "Fraction":
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.deno * other.deno)
        return Fraction(self.num * other, self.deno)

    def __repr__(self):
        if not self.num:
            return "0"
        if abs(self.deno) == 1:
            return str(self.num)
        return f"{self.num}/{self.deno}"


def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def substitute(self, ri, rj, c):
        print(f"R{rj}'->({c})*R{rj} {[x*c for x in self.matrix[rj - 1]]}")
        print(f"R{ri} ==> R{ri}-R{rj}'")
        ri -= 1
        rj -= 1
        self.matrix[ri] = [x - y * c for x, y in zip(self.matrix[ri], self.matrix[rj])]
        self.render()

    def scale(self, ri, c, opr):
        print(f"R{ri} => R{ri}{opr}({c})")
        ri -= 1
        self.matrix[ri] = [x * c.flip() for x in self.matrix[ri]]
        self.render()

    def render(self):
        for row in self.matrix:
            print("".join([f"{str(x):>8}" for x in row]))
        print()

    def __str__(self):
        return "[" + "\n ".join([str(x) for x in self.matrix]) + "]"

    def __getitem__(self, key):
        return self.matrix[key]


def back_substitution(matrix):
    ans = [0 for _ in range(matrix.rows)]
    for i in range(matrix.rows)[::-1]:
        ans[i] = matrix[i][-1]
        for j in range(i + 1, matrix.cols - 1):
            ans[i] -= matrix[i][j] * ans[j]
        ans[i] *= matrix[i][i]
    return ans


filename = input("Enter filename: ")
m = readMat(filename)
m = [[Fraction(int(y), 1) for y in x] for x in m]
matrix = Matrix(m)
print("Augmented Matrix:")
matrix.render()
for i in range(min(matrix.rows, matrix.cols)):
    matrix.scale(i + 1, matrix[i][i], "/")
    for j in range(i + 1, matrix.rows):
        if matrix[j][i].num:
            matrix.substitute(j + 1, i + 1, matrix[j][i])

print("Result from Gaussian Elimination:")
matrix.render()
print("After Back-Substitution:")
alphabet = "abcdefghijklmnopqrstuvwxyz"
x = back_substitution(matrix)
for i in range(len(x)):
    print(f"{alphabet[i]} = {x[i]}")
print()
