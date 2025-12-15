from abc import abstractmethod, ABC

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI Method")

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using CreditCard Method")

class DebitCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using DebitCard Method")

class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        return self.payment_strategy.pay(amount)


cart1 = ShoppingCart(CreditCard())
print(cart1.checkout(300))

cart2 = ShoppingCart(UPI())
print(cart2.checkout(3000))

