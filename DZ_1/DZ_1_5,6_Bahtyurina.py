# Задания 5 и 6
isderzhki = input("Введите издержки Компании, руб.: ")
dohod = input("Введите выручку Компании, руб.: ")
profit = float(dohod) - float(isderzhki)
if profit < 0:
    print("Компания терпит убытки")
elif profit ==0:
    print("Компания работает в 'ноль'")
else:
    print("Компания получила прибыль в размере {:.1f}".format(profit / 1000), "тыс.руб.")
    print("Рентабельность выручки: {:.2f}".format(profit / float(dohod) * 100), "%")
    shtat = int(input("Укажите численность персонала: "))
    print("Прибыль в расчете на одного сотрудника: %.2f" %(profit / shtat), "руб.")
