days = int(input("How many day : "))
sum = 0
for i in range(days):
    price = float(input(f"Input price in day {i+1} : "))
    sum += price*(0.95-0.01*i)

print(f"Summary price = {sum:.2f}")
