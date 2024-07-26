list1 = eval(input("Input list1: "))
list2 = eval(input("Input list2: "))


def difference(l1, l2):
    diff = []
    for item in l1:
        if not item in l2:
            diff.append(item)
    return diff


print(f"Missing values in list1 = {difference(list2,list1)}")
print(f"Additional values in list1 = {difference(list1,list2)}")
print(f"Missing values in list2 = {difference(list1,list2)}")
print(f"Additional values in list2 = {difference(list2,list1)}")
