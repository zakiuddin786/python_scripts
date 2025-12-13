class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance #private

    def deposit(self, amount):
        """Instance method - works with the instance data"""
        if amount>0: 
            self.__balance += amount
            return f"Amount {amount} deposited successfully in {self.account_holder}'s account"
        else:
            return f"{amount} is invalid deposite"
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Amount {amount} got withdrew from {self.account_holder}'s account"
        else:
            return f"Insufficient funds to withdraw {amount}"
        
    def get_balance(self):
        """this is to get the balance"""
        return f"{self.account_holder}'s balance is {self.__balance}"
    
account1 = BankAccount('Zaki', 100)
account2 = BankAccount("John", 1000000)
account3 = BankAccount("Rahul", 1000)

account1.__balance = 100000000000000

print(account1.withdraw(1000))
print(account2.withdraw(1000))
print(account3.withdraw(1000))
print(account1.get_balance())
print(account2.get_balance())
print(account3.get_balance())
print(account1.deposit(100000))
print(account2.deposit(3000))
print(account3.deposit(100000))
print(account1.get_balance())
print(account2.get_balance())
print(account3.get_balance())


