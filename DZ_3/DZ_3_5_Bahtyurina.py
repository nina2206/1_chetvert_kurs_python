# Задание 5
# Суммирование бесконечного количества вводимых чисел
def summa(new_digs_list):
    """Суммирует ряд целых чисел,
    игнорирует все <<не числа>>, кроме параметра выхода <q>
    """

    global my_sum, ex_q
    new_digs_list = new_digs_list.split(" ")
    for i in new_digs_list:
        if i == "q":
            ex_q = "q"
            return my_sum
            break
        else:
            if i.isdigit():
                my_sum += int(i)
    return my_sum

my_sum = 0
ex_q = ""
while True:
    if ex_q != "q":
        new_digs = input("Введите числа через пробел "
                     "или нажмите 'q'для завершения:\n")
        summa(new_digs)
        print(f"Текущий результат: {my_sum}. Продолжить...")
    else:
        break
print("Итоговая сумма: ", my_sum)
