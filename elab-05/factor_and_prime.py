def list_factors(n):
    """
    Get string of factors of n
    :params n is an integer to find factors
    :return string of factors (with a space between each factor)
    >>> list_factors(6)
    '1 2 3 6 '
    >>> list_factors(7)
    '1 7 '
    >>> list_factors(12)
    '1 2 3 4 6 12 '
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(str(i))
    return " ".join(factors)


def find_sum_and_num_factors(n):
    """
    Find summation and count number of factors of n
    :params n is an integer to find factors
    :return sum is summation of factors of n
            count is number of factors of n
    >>> find_sum_and_num_factors(6)
    (12, 4)
    >>> find_sum_and_num_factors(7)
    (8, 2)
    >>> find_sum_and_num_factors(12)
    (28, 6)
    """
    listf = list_factors(n).split()
    sum_of_factors = sum([int(x) for x in listf])

    return (sum_of_factors, len(listf))


num = int(input("Enter positive number: "))
listf = list_factors(num)
print(f"Factors of {num} are")
print(listf)
sf = find_sum_and_num_factors(num)
print(f"Sum of {listf} is {sf[0]}")
print(f"Number of factors is {sf[1]}")
if sf[1] == 2:
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")
