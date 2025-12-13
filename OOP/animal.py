class Dog:
    """A class representing a dog"""
    species = "Golden retriver" # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute (unique to each instance)
        self.age = age
        
    def introduce(self): # method
        return f"I am {self.name} {self.age} years old"
    
    def bark(self):
        return "Bow wow"
    
dog1 = Dog("sheru", 6)
dog2 = Dog("Shera", 8)

# accessing the attributes
print(dog1.name)
print(dog1.species)
print(dog2.species)
print(Dog.species)

print(dog2.name)

# calling the methods
print(dog1.introduce())
print(dog2.introduce())