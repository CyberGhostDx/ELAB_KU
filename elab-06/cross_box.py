n = int(input())

for i in range((n + 1) // 2):
    if i == 0:
        print("." * n)
        continue
    if i == (n - 1) / 2:
        print("." + " " * (i - 1) + "." + " " * (i - 1) + ".")
        continue
    print("." + " " * (i - 1) + "." + " " * (n - 2 * i - 2) + "." + " " * (i - 1) + ".")


for i in range(n // 2 - 1, -1, -1):
    if i == 0:
        print("." * n)
        continue
    print("." + " " * (i - 1) + "." + " " * (n - 2 * i - 2) + "." + " " * (i - 1) + ".")
