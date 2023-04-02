class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount

acc = Account(2000)
acc.deposit(500)
print(acc.getBalance())
acc.withdrawal(500)
print(acc.getBalance())  

