pos_nums = [0.0]
neg_nums = [0.0]
while 1:
    num = float(input("Enter a number (to exit, just enter 0): "))
    if num == 0:
        break
    elif num > 0:
        pos_nums.append(num)
    else:
        neg_nums.append(num)

print(f"The sum of positive numbers is {sum(pos_nums):.2f}")
print(f"The sum of negative numbers is {sum(neg_nums):.2f}")
