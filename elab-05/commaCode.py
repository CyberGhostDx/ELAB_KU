def commaCode(l):
    if len(l) == 0:
        return ""
    if len(l) > 1:
        return ", ".join(l[:-1]) + ", and " + l[-1]
    return l[0]


input_list = input("Input: ").split()

print(commaCode(input_list))
