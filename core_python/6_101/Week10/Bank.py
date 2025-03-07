class Bank:
    def __init__(self):
        self.accounts = {}

    def get_balance(self, account):
        return self.accounts.get(account, 0)

    def deposit(self, account, amount):
        self.accounts[account] = self.get_balance(account) + amount

    def withdraw(self, account, amount):
        balance = self.get_balance(account)
        if balance < amount:
            raise InsufficientFundsException("Insufficient balance")
        self.accounts[account] = balance - amount


class InsufficientFundsException(Exception):
    pass


b = Bank()
b.deposit("John", 2)
b.deposit("Dave", 3)
print(b.get_balance("John"))


def bank():
    accounts = {}

    def balance(account):
        return accounts.get(account, 0)

    def deposit(account, amount):
        accounts[account] = balance(account) + amount

    return balance, deposit


balance, deposit = bank()
deposit(123, 2)
print(balance(123))
