def factor_count(n):
    arr = [1, n]
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)
    return len(arr)
