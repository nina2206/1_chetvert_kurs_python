# Задание 3
# сумма чисел
some_num = input("Введите одну цифру: ")
# 1 способ, для трех слагаемых (решение задачи "в лоб")
summa =int(some_num) + int(some_num + some_num) + int(some_num + some_num + some_num)
print("Сумма составных чисел: ", summa)
# 2 способ (работает для n-количества слагаемых в сумме, каждое слагаемое может состоять из нескольких цифр)
some_num = input("Введите ещё число: ")
n = int(input("Сколько чисел нужно сложить? Укажите: "))
summa = int(some_num) #переменная суммы
schet = 1 #счетчик итераций
nov_chislo = some_num
while schet < n:
    nov_chislo = nov_chislo + some_num
    summa = summa + int(nov_chislo)
    schet += 1
print(f"Сумма составных чисел равна {summa}")
