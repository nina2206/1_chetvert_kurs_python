# Задание 1
# Функция деления чисел
def d_result1():
    """Возвращает результат деления двух чисел.

    Вар.1.В функции реализованы и ввод значений, и отработка результата
    """
    try:
        divident = float(input("Введите делимое: "))
        divider = float(input("Введите делитель: "))
    except ValueError:
        return "НЕВОЗМОЖЕНО: одно из введенных значений - не число"
    try:
        divident / divider
    except ZeroDivisionError:
        return "НЕВОЗМОЖЕНО: делитель равен нулю"
    return round(divident / divider, 2)

def d_result2(d1, d2):
    """Возвращает результат деления двух чисел.

    Вар.2. Функция с позиционными аргументами. Возвращает результат деления
    """
    try:
        d1, d2 = float(d1), float(d2)
        res = d1 / d2
    except (ValueError, ValueError):
        return "НЕВОЗМОЖЕНО: одно из введенных значений - не число"
    except ZeroDivisionError:
        return "НЕВОЗМОЖЕНО: делитель равен нулю"
    return round(res, 3)

print ("Результат деления #1: ", d_result1())
print("Результат деления #2: ", d_result2(input("Введите делимое: "), input("Введите делитель: ")))






