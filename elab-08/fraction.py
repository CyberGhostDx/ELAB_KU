class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.num = numerator // gcd(numerator, denominator)
        self.deno = denominator // gcd(numerator, denominator)

    def evaluate(self) -> float:
        return self.num / self.deno

    def add(self, n: int) -> "Fraction":
        return Fraction(self.num + n * self.deno, self.deno)

    def __add__(self, fraction_other: "Fraction") -> "Fraction":
        num = self.num * fraction_other.deno
        other_num = fraction_other.num * self.deno
        deno = self.deno * fraction_other.deno
        return Fraction(num + other_num, deno)

    def multiply(self, n: int) -> "Fraction":
        return Fraction(self.num * n, self.deno)

    def __mul__(self, fraction_other: "Fraction") -> "Fraction":
        return Fraction(self.num * fraction_other.num, self.deno * fraction_other.deno)

    def __toString__(self) -> str:
        if not self.num:
            return "0 / 1"
        return f"{self.num} / {self.deno}"

    def __str__(self):
        return self.__toString__()


def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)
