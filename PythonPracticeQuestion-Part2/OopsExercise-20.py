class BankAccount:
#    Accounts = {}
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, d_amount):
        self.balance += self.d_amount

    def withdraw(self, w_amount):
        if self.w_amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= self.w_amount
            print("Money Withdrawn from Bank Account")



