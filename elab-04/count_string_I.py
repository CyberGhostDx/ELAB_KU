strings = input("Enter a set of strings: ")


def countStr(str_list):
    count = 0
    for string in str_list:
        if len(string) > 1 and string[0] == string[-1]:
            count += 1
    return count


str_list = strings.split()
print(countStr(str_list))
