class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance
    
class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ayush", 500000)
print("Account title:", account.title)
print("Account balance:", account.balance)

savingsAccount = SavingsAccount("parekh", 500000, 5)
print("Savings account title:", savingsAccount.title)
print("Savings account balance:", savingsAccount.balance)
print("Savings account interest rate:", savingsAccount.interestRate)
