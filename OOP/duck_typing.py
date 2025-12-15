class Dog:
    def speak(self):
        print("Bow Wow")

class Cat:
    def speak(self):
        print("Meow Wow")

class Human:
    def speak(self):
        print("Hello")

def make_sound(entity):
    entity.speak()

make_sound(Dog())
make_sound(Cat())
make_sound(Human())

class PriceCalculator:
    def calculate(self, price, discount_type):
        if discount_type == "Student":
            return price * 0.9
        elif discount_type == "Alumini":
            return price * 0.8
        return price
