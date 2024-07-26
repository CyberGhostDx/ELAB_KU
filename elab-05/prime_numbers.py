def isPrime(number):
    """
    Check if the number is prime number
    :params number: is the number to check if is prime number
    :return: True if the number is prime number
             False if the number isn't prime number
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(1231)
    True
    >>> isPrime(14)
    False
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def printAllPrimes(limit):
    """
    Print all the prime number between 1 to the limit
    >>> printAllPrimes(10)
    2 3 5 7
    >>> printAllPrimes(20)
    2 3 5 7 11 13 17 19
    >>> printAllPrimes(0)

    >>> printAllPrimes(2)
    2
    >>> printAllPrimes(3)
    2 3
    """
    for i in range(1, limit + 1):
        if isPrime(i):
            print(i, end=" ")


number = int(input("Input n: "))
printAllPrimes(number)
