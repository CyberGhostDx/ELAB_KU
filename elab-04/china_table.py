def plus(total, value):
    return total + value


def minus(total, value):
    return total - value


n = int(input("How many food you have : "))
sum = 0

for i in range(n):
    food, opr = input().split()
    if opr == "1":
        sum = plus(sum, int(food))
    else:
        sum = minus(sum, int(food))

print(sum)
