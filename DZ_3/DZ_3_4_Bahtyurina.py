# Задание 4
# Возведение в отрицательную степень
def my_func1(x, y):
    """Проверяет значения и возводит в отрицательную степень.
    Вариант 1. Использует возведение в степень с помощью оператора **
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
         return "Не являются числами"
    if x <= 0 or y >= 0:
        return " Выход из функции: числа не удовлетворяют условиям ввода"
    else:
        return round(x ** y, 4)

def my_func2(x, y):
    """Проверяет значения и возводит в отрицательную степень.
    Вариант 2. Использует цикл
    """
    try:
         x = float(x)
         y = int(y)
    except ValueError:
         return "Не являются числами"
    if x <= 0 or y >= 0:
        return " Выход из функции: числа не удовлетворяют условиям ввода"
    else:
        res = 1 / x
        for i in range(1, abs(y)):
            res /= x
        return round(res, 4)

osnov = input("Введите основание (действительное положительное число): ")
st = input("Введите степень (целое отрицательное число): ")
print("Результат по варианту 1: ", my_func1(osnov, st))
print("Результат по варианту 2: ", my_func2(osnov, st))

