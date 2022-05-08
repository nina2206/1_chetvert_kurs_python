# Задание 2
# Класс-исключение , отрабатывает деление на ноль

class ZeroDiv(Exception):
    def __init__(self, err_massager):
        self.divider = err_massager

d_1 = 1000
d_2 = input("enter some number: ")
try:
    d_2 = int(d_2)
    if d_2 != 0:
        res = d_1 / d_2
    else:
        raise ZeroDiv("\033[31m Divider is Zero!")
except ValueError:
    print("Divider is a string of a text")
except ZeroDiv as zd:
    print(zd)
else:
    print(f"\033[32m Divizion is sucsessful. Resuls is {res:.2f}")