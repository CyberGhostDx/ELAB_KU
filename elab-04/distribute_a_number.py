def count_digits(number):
    return len(str(number))


def get_last_digit(n):
    return int(str(n)[-1])


def get_distribution(number):
    arr = []
    num_str = str(number)
    digits = count_digits(number)
    for i in range(digits):
        arr.append(f"{num_str[digits-i-1]}x10^{i}")
    return " + ".join(arr)


print(get_distribution(306))

# Main
number = int(input("Input number: "))
print(f"{number} = {get_distribution(number)}")
