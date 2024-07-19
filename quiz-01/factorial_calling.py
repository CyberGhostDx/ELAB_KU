n = int(input("Enter a positive integer n: "))
print(f">call fac({n})")


def fac(n):
    sum = 1
    for i in range(n):
        sum *= i + 1
    return sum


for i in range(n):
    if n == 0:
        print(1)
        break
    curr = " * ".join([str(i) for i in list(range(n, n - i - 1, -1))])
    print(" " + curr, end=" * ")
    print(f"fac({n-i-1})")

if n != 0 and n != 1:
    print(" " + " * ".join([str(i) for i in list(range(n, n - i, -1))]) + " * 1 * 1")

if n == 0:
    print(" 1")

if n == 1:
    print(" 1 * 1")

print(f">fac({n})={fac(n)}")
