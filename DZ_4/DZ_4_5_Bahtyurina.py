# Задание 5
# Генерация списка из четных чисел
# Произведение всех элементов списка

from random import randrange
from functools import reduce
def el_times_el(el1, el2):
    """Вычисляет произведение двух элементов"""
    return el1 * el2

new_list = [randrange(100, 1001, 2) for n in range(100, 1001)]

print("Исходный список:", new_list)
print("Произведение всех элементов списка:", reduce(el_times_el, new_list))