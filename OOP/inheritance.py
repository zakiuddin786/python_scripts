class Animal:
    def breathe(self):
        print("I'm Breathing")

    def speak(self):
        print("I'm an animal and I'm learning to speak")

class Dog(Animal): #Is-A relationship (single inheritance)
    def speak(self): # polymorphism
        super().speak()
        print("I'm a dog and I'm barking")

class Puppy(Dog): # multilevel inheritance
    def speak(self):
        print("I'm a puppy I'll call my parent to teach how to speak")
        super().speak()
        print("I learnt how to speak")

class Cat(Animal): #Is-A relationship # hieratchical inheritance
    def speak(self):
        super().speak() # allows the child to call the parents method
        print("I learnt how to say Mewo ")

class Flyer:
    def fly(self):
        print("I'm flying")
    def eat(self):
        print("I'm a flyer and I'm eating")

class Swimmer:
    def swim(self):
        print("I'm swimming")
    def eat(self):
        print("I'm a Swimmer and I'm eating")

class Duck(Swimmer, Flyer ):
    def eat(self):
        print("I'm duck and I'm eating")
    pass

dogie = Dog()
dogie.breathe()
dogie.speak()
catie = Cat()
catie.speak()
pup = Puppy()
pup.speak()

ducie = Duck()
print(Duck.mro()) # MEthod resolution order
ducie.fly()
ducie.swim()
ducie.eat()