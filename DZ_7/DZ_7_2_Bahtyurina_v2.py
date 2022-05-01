#Задание 2
# Расчет расхода ткани
# не получилось решение через __add__
from abc import ABC, abstractmethod
class Clothes(ABC):
    total_cloth_items = 0 #Счетчик кол-ва экзнмпляров одежды
    total_fabric = 0
    @abstractmethod
    def __init__(self):
        pass
    @property
    @abstractmethod
    def total_fabric(self):
        pass

    def __add__(self, other):
        return Clothes(self.total_fabric + other.total_fabric)

class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.__size = h
        Clothes.total_cloth_items += 1

    @property
    def total_fabric(self):
        return round(self.__size*2/100 + 0.3)


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.__size = v
        Clothes.total_cloth_items += 1

    @property
    def total_fabric(self):
        return round(self.__size/6.5 + 0.5)


coat_1 = Coat(50)
coat_2 = Coat(48)
coat_3 = Coat(46)
suit_1 = Suit(160)
suit_2 = Suit(150)
print(f"There's fabric for {Clothes.total_cloth_items} items: {Clothes.total_fabric} m")
