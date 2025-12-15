class Engine: 
    def start(self):
        print("Engine is started")

class Car:
    def __init__(self):
        self.engine = Engine() # Has - A relation

    def start(self):
        self.engine.start()
        print("Starting to move the car")

tarzan = Car()
tarzan.start()