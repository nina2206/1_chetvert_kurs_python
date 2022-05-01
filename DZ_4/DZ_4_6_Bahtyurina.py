# Задание 6
# Генерация списка, начиная с указанного числа
# Повтор элементов списка

from itertools import count
from itertools import cycle
new_list_1 = []
for n in count(20):
    if n <= 50:
        new_list_1.append(n)
    else:
        break
print("Первый список: \n", new_list_1)

fraza = "Ряд повторяющихся элементов"
n = 0
for el in cycle(fraza):
    if n < len(fraza):
        print(el, end='')
        n += 1
    else:
        break
