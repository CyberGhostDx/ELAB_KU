### define your function merge(a, b) in this yellow box
def merge(a, b):
    l = []
    l.extend(a)
    l.extend(b)
    if isinstance(l[0], int):
        for i in range(len(l)):
            for j in range(i + 1):
                if l[i] < l[j]:
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
    else:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                count = 0
                if len(l[i]) > 1 and len(l[j]) > 1:
                    while l[i][count] == l[j][count]:
                        count += 1
                if l[i][count] > l[j][count]:
                    tmp = l[i]
                    l[i] = l[j]
                    l[j] = tmp
    return l


def getInput():
    a = eval(input("Enter list a: "))
    b = eval(input("Enter list b: "))
    return a, b


### main begins here
a, b = getInput()
res = merge(a, b)
print(res)
