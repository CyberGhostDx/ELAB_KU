n = int(input("Input number: "))

for i in range(1, n + 1):
    print(" ".join([str(s) for s in range(1, i + 1)]))
