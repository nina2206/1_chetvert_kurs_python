#Задание 2
# Расчет расхода ткани
from abc import ABC, abstractmethod
class Clothes(ABC):
    total_cloth_items = 0 #Счетчик кол-ва экзнмпляров одежды
    total_cloth_fabric = 0 # Счетчик общего расхода ткани
    @abstractmethod
    def __init__(self, param):
        self.__size = param
    @property
    @abstractmethod
    def total_fabric(self):
        pass


class Suit(Clothes):
    def __init__(self, h):
        self.__size = h
        Clothes.total_cloth_items += 1
        Clothes.total_cloth_fabric += self.total_fabric
    @property
    def size(self):
        return self.__size

    # сеттер для создания свойств
    @size.setter
    def year(self, size):
        """Отсекает нестандартные размеры одежды и приводит их к диапазону стандартных"""
        if size < 98:
            self.__size = 98
        elif size > 180:
            self.__size = 180
        else:
             self.__size = size

    @property
    def total_fabric(self):
        return round(self.__size*2/100 + 0.3)

    def __str__(self):
        tot = Suit.total_fabric
        return f"Расход ткани на костюм: {tot} м"

class Coat(Clothes):
    def __init__(self, v):
        self.__size = v
        Clothes.total_cloth_items += 1
        Clothes.total_cloth_fabric += self.total_fabric
    @property
    def size(self):
        return self.__size

    @size.setter
    def year(self, size):
        """Отсекает нестандартные размеры одежды и приводит их к диапазону стандартных"""
        if size < 32:
            self.__size = 32
        elif size > 60:
            self.__size = 60
        else:
             self.__size = size

    @property
    def total_fabric(self):
        return round(self.__size/6.5 + 0.5)


coat_1 = Coat(50)
coat_2 = Coat(48)
coat_3 = Coat(46)
suit_1 = Suit(160)
suit_2 = Suit(150)
print(f"There's fabric for {Clothes.total_cloth_items} items: {Clothes.total_cloth_fabric} m")





