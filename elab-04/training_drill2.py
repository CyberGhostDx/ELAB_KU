days = int(input("Day: "))

shoot = [1, 1]
for i in range(2, days):
    shoot.append(shoot[i - 1] + shoot[i - 2])

if days == 1:
    print(1)
else:
    print(" ".join([str(x) for x in shoot]))
