def fibo(n, memo):
    if n == 1 or n == 2:
        return 1
    if not n in memo:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


print(fibo(100, {}))
