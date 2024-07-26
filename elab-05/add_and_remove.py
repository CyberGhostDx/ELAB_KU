l = list(map(int, input().split()))
while 1:
    menu, x = input().split()
    x = int(x)
    if menu == "E":
        break
    if menu == "A":
        l.append(x)
    if menu == "S":
        print(l[x])
    if menu == "R":
        l.pop(x)

print(" ".join([str(x) for x in l]))
