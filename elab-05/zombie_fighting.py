n, m = list(map(int, input().split()))

t = []
time = 1
kill = 0

for i in range(n):
    t.append(int(input()))

while kill < m:
    kill_list = len([1 for x in t if time % x == 0])
    if kill_list:
        kill += kill_list
    time += 1

print(time - 1)
