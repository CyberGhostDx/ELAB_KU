def simple_interest(p, r, t):
    return p * (1 + r / 100 * t)


def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t


p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))
