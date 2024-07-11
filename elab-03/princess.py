def caltime(s):
    h = s // 60 // 60
    m = s // 60 % 60
    second = s % 60
    return (h, m, second)


s = int(input("s: "))

time = caltime(s)

print(
    f"{s} seconds equals {time[0]} hour(s) {time[1]} minute(s) and {time[2]} second(s)"
)
