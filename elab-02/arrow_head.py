n = int(input("Input number: "))

while n % 2 == 0:
    print("Please input odd number")
    n = int(input("Input number: "))


for i in range(1, n + 1):
    print("x" * i)
for i in range(1, n + 1):
    print("x" * (n - i))
