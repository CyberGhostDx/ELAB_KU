nums = []


while 1:
    x = int(input())
    if x == 0:
        break
    nums.append(x)

count = 0
prv = nums[0]
max_num = nums[0]
max_count = 0

for i in range(1, len(nums) - 1):
    if nums[i] == prv:
        count += 1
    if count > max_count:
        max_num = nums[i]
        max_count = count
    if nums[i] != prv:
        count = 0
    prv = nums[i]

print(max_count + 1)
print(max_num)
