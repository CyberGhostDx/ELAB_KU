n = int(input("N: "))
m = int(input("M: "))

remains = []

for i in range(n):
    num = int(input(f"Input number {i+1}: "))
    remain = num % m
    if not remain in remains:
        remains.append(remain)

print(len(remains))
