class User:
    def __init__(self, age, user_id, name):
        self.age = age
        self._user_id = user_id
        self.name = name
        self._profile = None

    @property
    def age(self): #getter
        return self._age 
    
    @age.setter # validation
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property 
    def user_id(self):
        return self._user_id
    
    @property
    def profile(self):
        if self._profile is None:
            print("Fetching the user profile from database")
            self._profile = {"city": "Hyd", "occupation": "Engineer"}
        return self._profile

user1 = User(30, 10098, "Zaki")
# user2 = User(-30) This is not possible and raises ValueError: Age cannot be negative
# user3 = User(0)
print(user1.user_id)
# user1.user_id = 98898 AttributeError: can't set attribute

print(f"Age of user 1 is {user1.age}")
# print(f"Age of user 2 is {user2.age}")
user1.age = 20
print(user1.age)
# user1.age = -20 ValueError: Age cannot be negative
print(user1.age)
print(user1.profile)
print(user1.profile)
print(user1.profile)
print(user1.profile)
print(user1.profile)


# print(f"Age of user 3 is {user3.age}")

class Employee:
    def __init__ (self, monthly_salary):
       self._monthly_salary = monthly_salary

    @property
    def salary(self):
        return self._monthly_salary * 12
        # return self.salary * 12 dont refer the property this way RecursionError: maximum recursion depth exceeded
    
    
emp1 = Employee(30000)
print(emp1.salary)

class Distance: 
    def __init__(self, meters):
        self._meters = meters
    
    @property
    def km(self):
        return self._meters / 1000
    
    @km.setter
    def km(self, value):
        self._meters = value * 1000

dist1 = Distance(8000)
print(dist1.km)
dist1.km = 80
print(dist1._meters)