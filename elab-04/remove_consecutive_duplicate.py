arr = eval(input("InputList: "))

remove_duplicated = []

for i, item in enumerate(arr):
    if i == 0:
        remove_duplicated.append(item)
        continue
    if item == arr[i - 1]:
        continue
    remove_duplicated.append(item)

print(remove_duplicated)
