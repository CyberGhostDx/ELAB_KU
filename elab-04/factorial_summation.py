def factorial(x):
    sum = 1
    for i in range(1, x + 1):
        sum *= i
    return sum


def fac_sum_distribute(k):
    sum = 0
    for i in range(1, k + 1):
        fac = factorial(i)
        sum += fac
        print(f"{i}! = {fac}")
    return sum


k = int(input("Input k: "))
print(f"Summation of factorial 1!-{k}! = {fac_sum_distribute(k)}")
