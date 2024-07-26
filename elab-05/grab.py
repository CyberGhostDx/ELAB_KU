from math import ceil

p = list(map(int, input().split()))

party = sum(p)

print(ceil(party / 4))
