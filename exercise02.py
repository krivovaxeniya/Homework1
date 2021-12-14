from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, params):
        self.params = params

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coats(Clothes):
    @property
    def consumption(self):
        return self.params / 6.5 + 0.5

class Suits(Clothes):
    @property
    def consumption(self):
        return 2 * self.params + 0.3

coat = Coats(20)
suit = Suits(35)
print(coat + suit)
