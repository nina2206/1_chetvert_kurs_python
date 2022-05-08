#Задания 4, 5, 6
#Склад оргтехники
from abc import ABC, abstractmethod
from random import randint
class ErrMassage(Exception):
    def __init__(self, text):
        self.error_massager = text

class OfficeEquipment(ABC):
    total_items = 0 #считает кол-во экземпляров

    @abstractmethod
    def __init__(self, wms, brand, manufacture):
        """Список обязательных атрибутов для экземпляров классов-наследников"""
        self.wms = wms
        self.brand = brand
        self.manufacture = manufacture
    @abstractmethod
    def __str__(self):
        """Вывод деталей объекта в аналитику"""
        pass

class Xerox(OfficeEquipment):
    def __init__(self, wms, brand, manufacture, speed):
        super().__init__(wms, brand, manufacture)
        self.speed = abs(float(speed))
        Warehouse.xeroxes.update({wms: 0})
        OfficeEquipment.total_items += 1

    def __str__(self):
        return f"{self.wms:0{4}}\t{self.brand}\t{self.manufacture}\t{self.speed}\n"

class Scanner(OfficeEquipment):
    def __init__(self, wms, brand, manufacture, resolution):
        super().__init__(wms, brand, manufacture)
        self.resolution = abs(float(resolution))
        Warehouse.scanners.update({wms: 0})
        OfficeEquipment.total_items += 1

    def __str__(self):
        return f"{self.wms:0{4}}\t{self.brand}\t{self.manufacture}\t{self.resolution}\n"

class Printer(OfficeEquipment):
    def __init__(self, wms, brand, manufacture, coloured):
        super().__init__(wms, brand, manufacture)
        self.coloured = True if coloured == "Y" else False
        Warehouse.printers.update({wms: 0})
        OfficeEquipment.total_items += 1

    def __str__(self):
        return f"{self.wms:0{4}}\t{self.brand}\t{self.manufacture}\t{self.coloured}\n"

class Warehouse:
    # группы оргтехники для учета складских остатков
    xeroxes = {}
    scanners = {}
    printers = {}

    @staticmethod
    def show_stock_ramains():
        """Возвращает сводную складских остатков по группам оргтехники"""
        return f"\033[36mStock datails:\n Scanners\tPrinters\tXeroxes\n{sum(Warehouse.scanners.values()):7d}" \
               f"\t{sum(Warehouse.printers.values()):8d}\t{sum(Warehouse.xeroxes.values()):10d}\033[0m"

    @staticmethod
    def stock_add():
        """Пополнение запасов на складе"""
        print("Enter new arrivals")
        for k in Warehouse.xeroxes.keys():
            pcs_of_equipment = validation(input(f"WMS {k:0{4}}: "))
            Warehouse.xeroxes[k] += int(pcs_of_equipment)
        for k in Warehouse.scanners.keys():
            pcs_of_equipment = validation(input(f"WMS {k:0{4}}: "))
            Warehouse.scanners[k] += int(pcs_of_equipment)
        for k in Warehouse.printers.keys():
            pcs_of_equipment = validation(input(f"WMS {k:0{4}}: "))
            Warehouse.printers[k] += int(pcs_of_equipment)

    @staticmethod
    def stock_reduction(group, pcs_of_equipment):
        "Уменьшение остатков на складе после передачи техники в подразделение"
        while pcs_of_equipment > 0:
            if group == "1":
                for k in Warehouse.xeroxes.keys():
                    if Warehouse.xeroxes[k] <= pcs_of_equipment:
                        pcs_of_equipment -= Warehouse.xeroxes[k]
                        Warehouse.xeroxes[k] = 0
                    else:
                        Warehouse.xeroxes[k] -= pcs_of_equipment
                        pcs_of_equipment = 0
            elif group == "2":
                for k in Warehouse.printers.keys():
                    if Warehouse.printers[k] <= pcs_of_equipment:
                        pcs_of_equipment -= Warehouse.printers[k]
                        Warehouse.printers[k] = 0
                    else:
                        Warehouse.printers[k] -= pcs_of_equipment
                        pcs_of_equipment = 0
            elif group == "3":
                for k in Warehouse.scanners.keys():
                    if Warehouse.scanners[k] <= pcs_of_equipment:
                        pcs_of_equipment -= Warehouse.scanners[k]
                        Warehouse.scanners[k] = 0
                    else:
                        Warehouse.scanners[k] -= pcs_of_equipment
                        pcs_of_equipment = 0

class Users:
    def __init__(self, code):
        self.code = code
        self.balanse = {"(1)Xeroxes": 0, "(2)Printers": 0, "(3)Scanners": 0}

    def __str__(self):
        return f"\033[33m{self.code} has office equipment:\n{self.balanse}\033[0m\n"

    def get_equipment(self, group):
        "Поступление орг.техники в подразделение"
        pcs_of_equipment = validation(input("How much units do you need?___"))
        pcs_of_equipment = int(pcs_of_equipment)
        try:
            if group == "1":
                if pcs_of_equipment <= sum(Warehouse.xeroxes.values()):
                   self.balanse["(1)Xeroxes"] += pcs_of_equipment
                   Warehouse.stock_reduction(group, pcs_of_equipment)
                else:
                    raise ErrMassage(f"There no {pcs_of_equipment} on stocks")
            elif group == "2":
                if pcs_of_equipment <= sum(Warehouse.printers.values()):
                   self.balanse["(2)Printers"] += pcs_of_equipment
                   Warehouse.stock_reduction(group, pcs_of_equipment)
                else:
                    raise ErrMassage(f"There no {pcs_of_equipment} on stocks")
            elif group == "3":
                if pcs_of_equipment <= sum(Warehouse.scanners.values()):
                   self.balanse["(3)Scanners"] += pcs_of_equipment
                   Warehouse.stock_reduction(group, pcs_of_equipment)
                else:
                    raise ErrMassage(f"There no {pcs_of_equipment} on stocks")
            else:
                print("Enter your request again")
        except ErrMassage as err_mass:
            print(f"\033[31m {err_mass}\033[0m")


def validation(som_num):
    """Пропускает в дальнейшую обработку только цифры, где есть такое требование к вводным"""
    while som_num.isdigit() == False:
        try:
            if som_num.isdigit() == True:
                break
            else:
                raise ErrMassage("This atribute should be a number.")
        except ErrMassage as err_mass:
            print(f"\033[31m {err_mass}\033[0m")
        som_num = input("Try again: ")
    return som_num

# Департаменты, в которые нужно раздать орг.технику
dep1 = Users("Sales Department")
dep2 = Users("Human Resourse")
dep3 = Users("Logistics Department")
# Создание базы закупаемой оргтехники
print("\033[36mLet's create Office Eqipment database. Update items with following patamertres:\033[0m".center(50))
print('{:>10}{:>20}{:>20}{:>20}'.format("WMS", "BRAND", "MANUFACTURE", "SPESIFICATION"))
scan1 = Scanner(randint(1, 30), input("enter brand: "), input("enter manufacture:"), validation(input("enter resolution:")))
scan2 = Scanner(randint(1, 30), input("enter brand: "), input("enter manufacture: "), validation(input("enter resolution")))
xser1 = Xerox(randint(31, 60), input("enter brand: "), input("enter manufacture: "), validation(input("enter speed:")))
xser2 = Xerox(randint(31, 60), input("enter brand: "), input("enter manufacture: "), validation(input("enter speed:")))
xser3 = Xerox(randint(31, 60), input("enter brand: "), input("enter manufacture: "), validation(input("enter speed:")))
prin1 = Printer(randint(61, 90), input("enter brand: "), input("enter manufacture: "), input("'Y' if colored"))
prin2 = Printer(randint(61, 90), input("enter brand: "), input("enter manufacture: "), input("'Y' if colored"))
prin3 = Printer(randint(61, 90), input("enter brand: "), input("enter manufacture: "), input("'Y' if colored"))

print(f"\033[36mOffice Equimpent include {OfficeEquipment.total_items} items:"
      f"\n{scan1}{scan2}{prin1},{prin2}{prin3}{xser1}{xser2}{xser3}\033[0m")

# Оприходование закупленной орг.техники
esc = ""
while esc != "q":
    print("___new arrivals get on stock___")
    Warehouse.stock_add()
# статистика остатков на складе по группам орг.техники
    print(f"\033[33mFree storage of office equipment:\n {Warehouse.show_stock_ramains()}")
# передача оргтехники в подразделения
    of_eq_group = ""
    while of_eq_group != "q":
        of_eq_group = validation(input(f"{dep1.code}, what kind of equipment do you need:\n"
                             f" 1 - xeroxes; 2 - printers, 3 - scanners"))
        dep1.get_equipment(of_eq_group)
        of_eq_group = input(f"'q' to go to next department or enother key to continue with {dep1.code}").lower()
    print(f"\033[33mFree storage of office equipment:\n {Warehouse.show_stock_ramains()}")
    of_eq_group = ""
    while of_eq_group != "q":
        of_eq_group = validation(input(f"{dep2.code}, what kind of equipment do you need:\n"
                             f" 1 - xeroxes; 2 - printers, 3 - scanners"))
        dep2.get_equipment(of_eq_group)
        of_eq_group = input(f"'q' to go to next department or enother key to continue with {dep2.code}").lower()
    print(f"\033[33mFree storage of office equipment:\n {Warehouse.show_stock_ramains()}")
    of_eq_group = ""
    while of_eq_group != "q":
        of_eq_group = validation(input(f"{dep3.code}, what kind of equipment do you need:\n"
                             f" 1 - xeroxes; 2 - printers, 3 - scanners"))
        dep3.get_equipment(of_eq_group)
        of_eq_group = input(f"'q' to go to next department or enother key to continue with {dep3.code}").lower()
    print(f"\033[33mFree storage of office equipment:\n {Warehouse.show_stock_ramains()}")
    print(dep1, dep2, dep3)
    print(f"Full list of stoks: {Warehouse.scanners}\t{Warehouse.printers}\t{Warehouse.xeroxes}")
    esc = input("enter 'q' to exit or enother key to restock").lower()

print(f"Full list of stocks: {Warehouse.scanners}\t{Warehouse.printers}\t{Warehouse.xeroxes}")
print("The end")

