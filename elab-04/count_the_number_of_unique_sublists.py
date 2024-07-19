arr = eval(input("Input: "))

items = {}

for l in arr:
    item = str(l)
    if not item in items:
        items[item] = 0
    items[item] += 1

sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

for item in sorted_items:
    key, value = item
    print(f"{key}: {value}")
