objects = eval(input("Enter a list of objects: "))


def countConsec(arr):
    if len(arr) == 0:
        return
    consecutive = [[arr[0], 1]]
    con_index = 0
    prv = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == prv:
            consecutive[con_index][1] += 1
        else:
            consecutive.append([arr[i], 1])
            con_index += 1
        prv = arr[i]
    return [(x, y) for x, y in consecutive]


consec = countConsec(objects)

if consec:
    max_con_sec = max(consec, key=lambda x: x[1])
    print(max_con_sec[0])
    print(max_con_sec[1])
else:
    print("Nothing to do.")
