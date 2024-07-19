nums = []
while 1:
    num = input("Enter a number (just [Enter] to quit): ")
    if not num:
        break
    nums.append(float(num))

if len(nums):
    nums_min = min(nums)
    nums_max = max(nums)
    nums_avg = sum(nums) / len(nums)

    print(f"Maximum is {nums_max:.2f}")
    print(f"Minimum is {nums_min:.2f}")
    print(f"Average is {nums_avg:.2f}")
else:
    print("Nothing to do.")
