arr = list(map(int, input().split()))


def is_invalid_input(f, arr):
    return not (-len(arr) <= f <= len(arr) - 1)


while 1:
    x, y = list(map(int, input().split()))
    if x < 0 and y < 0 and x > y:
        break
    if x < 0 and y >= 0 and y < len(arr) - abs(x):
        break
    if (x > y and y >= 0) and not (y < 0 and x > len(arr) - abs(y)):
        break
    if is_invalid_input(x, arr) and is_invalid_input(y, arr):
        print("x and y Bad Input")
        continue
    if is_invalid_input(x, arr):
        print("x Bad Input")
        continue
    if is_invalid_input(y, arr):
        print("y Bad Input")
        continue
    if y != -1:
        print(sum(arr[x : y + 1]))
    else:
        print(sum(arr[x:y]) + arr[y])
