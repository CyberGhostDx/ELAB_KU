def myzip(m, n):
    nl = []
    if len(m) != len(n):
        return []
    for i in range(len(m)):
        nl.append(m[i] + n[i])
    return nl
