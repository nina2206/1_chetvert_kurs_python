# Задание 1
# Расчет заработной платы

def func_zp(p_1, p_2, p_3):
    """Рассчитывает з.п. по формуле (выработка в часах * ставка в час) + премия"""
    try:
        p_1, p_2, p_3 = float(p_1), float(p_2), float(p_3)
    except ValueError:
        return "Некорректные аргументы"
    if p_1 < 0 or p_2 < 0 or p_3 < 0:
        return "Аргументы не должны быть отрицательными"
    else:
        return p_1 * p_2 + p_3

from sys import argv
mod_name, p1, p2, p3 = argv

print("Выработка, ч: ", p1)
print("Почасовая ставка, руб.: ", p2)
print("Премиальные, руб.: ", p3)
print("З/п сотрудника, руб:", func_zp(p1, p2, p3))
