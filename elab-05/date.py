d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

days = 0


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


if is_leap_year(y) and m > 2:
    days += 1

for i in range(1, m):
    if i % 2 == 0 and i != 2:
        days += 30
    elif i == 2:
        days += 28
    else:
        days += 31

days += d

print(days)
