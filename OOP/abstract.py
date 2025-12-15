from abc import abstractmethod, ABC

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI Method")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using CreditCard Method")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using DebitCard Method")


def checkout(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)

checkout(UPI(), 900)
checkout(CreditCard(), 9000)
checkout(DebitCard(), 7000)

# without abstraction and it will be requiring modification at every step
def checkout_without_abstraction(method, amount):
    if method == "UPI":
        UPI.pay(amount)
    elif method == "Credit_card":
        CreditCard.pay()

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print(f"Mysql DB connected")


class MongoDB(Database):
    def connect(self):
        print(f"Mongo DB connected")


class PostGress(Database):
    def connect(self):
        print(f"Mongo DB connected")