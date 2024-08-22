class BankAccount:
    def __init__(self, accountID="1001", balance=500):
        self.accountID = accountID
        self.balance = balance

    def set_account_ID(self, newID):
        self.accountID = newID

    def set_balance(self, new_balance):
        self.balance = new_balance

    def get_account_ID(self):
        return self.accountID

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
