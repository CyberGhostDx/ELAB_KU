numbers = []
for _ in range(3):
    numbers.append(int(input()))


def sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print(" ".join([str(n) for n in sort(numbers)]))
