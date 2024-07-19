original_list = eval(input("Original list: "))
flatten = []
temp = original_list.copy()

is_not_flatten = True
while is_not_flatten:
    for x in temp:
        if isinstance(x, list):
            flatten.extend(x)
        else:
            flatten.append(x)
    for x in flatten:
        if isinstance(x, list):
            temp = flatten
            flatten = []
            break
    else:
        is_not_flatten = False

print(f"Flatten list: {flatten}")
