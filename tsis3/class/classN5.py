class Account:
    def __init__(self, o, b):
        self.owner = o
        self.balance = b
    def deposit(self, d):
        self.balance += d
        print("Your current balance:", self.balance)
    def withdraw(self, w):
        if self.balance - w < 0:
            print("Insufficient funds on the account")
            return 0
        self.balance -= w
        print("Your current balance:", self.balance)
myaccount = Account(input(), int(input()))
myaccount.deposit(int(input()))
myaccount.deposit(int(input()))
myaccount.withdraw(int(input()))
myaccount.withdraw(int(input()))