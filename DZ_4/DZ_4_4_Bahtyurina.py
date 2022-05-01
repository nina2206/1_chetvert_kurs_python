# Задание 4
# Чистка списка от повторяющихся элементов

from random import randint
new_list = [randint(0, 100) for n in range(0, 50)]
print("Исходный список: \n", new_list)

final_list = [n for n in new_list if new_list.count(n) == 1]
print("Отобранный список: \n", final_list)