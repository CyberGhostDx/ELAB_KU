class Coin:
    def __init__(self, value=1):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Coin"


class BankNote:
    def __init__(self, value=20):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Banknote"


moneys = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

amount = int(input("Input amount : "))

for money in moneys:
    if money <= amount:
        if amount >= 20:
            change = amount // money
            amount %= money
            print(f"You get {change} of {BankNote(money)}")
        else:
            change = amount // money
            amount %= money
            print(f"You get {change} of {Coin(money)}")
