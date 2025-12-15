class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
        return cls._instance
    
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

class Database: 
    _instance = None

    def __new__(cls): # This will be making sure the class is not reinstantiated
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        return cls._instance
    
    def connect(self):
        if not self._connected:
            self._connected = True
            return "Connected to database"
        return "Already connected"

db1 = Database()
db2 = Database()
print(db1.connect())
print(db2.connect())
