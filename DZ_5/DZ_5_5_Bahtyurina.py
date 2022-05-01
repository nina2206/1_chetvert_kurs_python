# запись чисел в файл и расчет суммы
from random import randint
with open("test2.txt", "w+", encoding="utf-8") as my_fi:
    my_fi.writelines([" ".join(str(randint(1, 100))) for dig in range(101)])
    my_fi.seek(0)
    print(f"Сумма чисел по строке: {sum(map(int, my_fi.readline().split()))}")