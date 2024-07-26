str1 = input("Input string: ")
str2 = input("Input string: ")


def intersect(l1, l2):
    intersect_list = []
    for item in l1:
        if item in l2 and not item in intersect_list:
            intersect_list.append(item)
    return intersect_list


for intersect_alpha in intersect(str1, str2):
    str1 = str1.replace(intersect_alpha, "")
    str2 = str2.replace(intersect_alpha, "")

print(str1 + str2)
