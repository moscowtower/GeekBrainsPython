from abc import ABC


class Vetement(ABC):
    def __init__(self, name):
        self.name = name

    def calc_fabric(self):
        pass

class Coat(Vetement):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def calc_fabric(self):
        return f'Потребуется {((int(self.size)/6.5)+0.5).__round__(3)} м ткани для пальто размером {self.size}'


class Suit(Vetement):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def calc_fabric(self):
        return f'Потребуется {(int(self.height)*2)+0.3} см ткани для костюма на рост {self.height}'

coat = Coat('Chanel', 11)
print(coat.calc_fabric)

suit = Suit('Armani', 185)
print(suit.calc_fabric)
