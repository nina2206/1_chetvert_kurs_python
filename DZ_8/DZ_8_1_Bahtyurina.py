# Задание 1
# Работа с датами
import re

class MyDate:
    def __init__(self, some_date):
        self.some_date = some_date
    @classmethod
    def date_to_int(cls, my_date):
        """Преобразует элементы даты в целочисленный формат"""
        return [int(el) for el in my_date.split("-")]
    @staticmethod
    def date_val(my_date):
        """Позволяет исправить ошибки в дате"""
        list_for_validation = MyDate.date_to_int(my_date)
        if list_for_validation[2] <= 1900 or list_for_validation[2] >= 2100:
            y = list_for_validation[2]
            list_for_validation.remove(y)
            list_for_validation.insert(2, int(input("enter correct year, 1900-2100: ")))
        if list_for_validation[1] > 12 or list_for_validation[1] < 1:
            m = list_for_validation[1]
            list_for_validation.remove(m)
            list_for_validation.insert(1, int(input("enter correct month, 1-12: ")))
        if list_for_validation[0] < 1 or list_for_validation[0] > 31:
            d = list_for_validation[0]
            list_for_validation.remove(d)
            list_for_validation.insert(0, int(input("enter correct day of the month 1-31: ")))
        else:
            print("\033[32m date is OK now \033[0m")
            return "-".join(map(str, list_for_validation))

my_date = input("enter some date, dd-mm-yyyy: ")
# Проверка даты на соответствие маске ввода
while re.match(r'\d{2}-\d{2}-\d{4}', my_date) == None:
        if re.match(r'\d{2}-\d{2}-\d{4}', my_date):
             break
        else:
            print("\033[31m format is uncorrect! try one more time! \033[0m")
            my_date = input("enter some date, dd-mm-yyyy: ")

print(MyDate.date_to_int(my_date))
print(MyDate.date_val(my_date))
