class BankAccount:
#    Accounts = {}
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, d_amount):
        self.balance +=  d_amount
        print("Deposit Done Successfully")

    def withdraw(self, w_amount):
        if w_amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= w_amount
            print("Money Withdrawn from Bank Account")

    def bankFees(self):
        fees =  self.balance * .05
        self.balance = self.balance - fees

    def display(self):
        print("The bank account number is {}".format(self.accountNumber))
        print("Name of Account holder is {}".format(self.name))
        print("Account Balance is {}".format(self.balance))

newaccount = BankAccount(12345, 'Mukul', 5000)
newaccount.deposit(1000)
newaccount.display()

newaccount.withdraw(500)
newaccount.display()


