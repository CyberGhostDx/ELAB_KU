# 0 - 9999
def digit(n):
    return int(str(n)[-1])


def tens(n):
    if n < 10:
        return 0
    return int(str(n)[-2])


def hundreds(n):
    if n < 100:
        return 0
    return int(str(n)[-3])


def thousands(n):
    if n < 1000:
        return 0
    return int(str(n)[0])


def sum_digits(n):
    return thousands(n) + hundreds(n) + tens(n) + digit(n)
