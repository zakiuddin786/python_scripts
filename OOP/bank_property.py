class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposite(self, amount):
        if amount <=0:
            raise ValueError("Deposite amount must be a positive number")
        self._balance += amount

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawal amount must be a positive value")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount

account1 = BankAccount()
print(account1.balance)

account1.deposite(10000)
print(account1.balance)
# account1.withdraw(100000) Raises a ValueError: Insufficient funds
print(account1.balance)
account1.withdraw(5000)
print(account1.balance)
account1.balance = 1000000
# print(account1.balance) AttributeError: can't set attribute 
