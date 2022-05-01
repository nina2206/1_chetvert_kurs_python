# Задание 2
# Генерирует список и реализует отбор элементов в новый список по условию
# условие отбора: значение элемента больше значения предыдущего элемента

from random import randint
new_list = [randint(0, 100) for n in range(0, 50)]
print("Исходный список: \n", new_list)

it = iter(new_list[:len(new_list)-1])
final_list = [n for n in new_list[1:] if n > next(it)]
print("Отобранный список: \n", final_list)