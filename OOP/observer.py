from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def deattach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for obsever in self._observers:
            obsever.update(self)

    def set_state(self, state):
        self._state = state
        self.notify()

class ConcreteObserver(Observer):
    def __init__(self, name ):
        self.name = name

    def update(self, subject):
        print(f"{self.name} received an update on change : {subject._state}")

subject = Subject()

observer1 = ConcreteObserver("Ob 1")
observer2 = ConcreteObserver("Ob 2")
observer3 = ConcreteObserver("Ob 3")

subject.attach(observer1)
subject.attach(observer2)
subject.attach(observer3)

subject.set_state("This is a new state being made to test observability")
