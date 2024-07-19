def alternatingSum(n):
    if n % 2 == 0:
        r = n // 2
    else:
        r = n // 2 + 1
    d = n // 2
    sum = r * r - (d + d * d)
    return sum


n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, alternatingSum(n)))
