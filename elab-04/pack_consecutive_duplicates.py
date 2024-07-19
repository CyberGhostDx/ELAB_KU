arr = eval(input("InputList: "))

packed = []

count = 0

for i, item in enumerate(arr):
    if i == 0:
        packed.append([item])
        continue
    if arr[i - 1] == item:
        packed[count].append(item)
    else:
        packed.append([item])
        count += 1

print(packed)
