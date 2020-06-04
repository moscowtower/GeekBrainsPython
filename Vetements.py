from abc import ABC, abstractmethod

class Vetement(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_fabric(self):
        pass

    def calc_total(self, other):
        return f'Суммарно {int(self.calc_fabric) + int(other.calc_fabric)}м ткани для {self.name} и {other.name}'


class Coat(Vetement):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def calc_fabric(self):
        result = (int(self.size)/6.5+0.5).__round__(3)
        return result

    def __str__(self):
        return f'Потребуется {self.calc_fabric}м ткани на размер {self.size} для {self.name}'


class Suit(Vetement):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def calc_fabric(self):
        result = ((int(self.height)*2)+0.3 / 100).__round__(3)
        return result

    def __str__(self):
        return f'Потребуется {self.calc_fabric}м ткани на рост {self.height}см для {self.name}'

coat = Coat('Chanel', 11)
print(coat)

suit = Suit('Armani', 185)
print(suit)

print(Vetement.calc_total(coat, suit))
