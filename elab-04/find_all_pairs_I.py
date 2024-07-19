nums = input("Enter list of number: ")
nums_list = nums.split()
nums_list = [int(x) for x in nums_list]
arr = []

for i in range(len(nums_list)):
    for j in range(i + 1, len(nums_list)):
        if abs(nums_list[i] - nums_list[j]) == 3:
            arr.append([nums_list[i], nums_list[j]])


print(f"Output list: {arr}")
