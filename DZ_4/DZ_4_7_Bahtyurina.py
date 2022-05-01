# Задание 7
# Вычисляет факториал часла

def fact(n):
    i = 1
    f = 1
    while i <= n:
        f *= i
        yield f, i
        i += 1

dig = int(input("Введите число: "))
for el, i in fact(dig):
    print (f"{i}!: {el}")

