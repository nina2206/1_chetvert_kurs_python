#Задание 3
# Создание списка из чисел
class ErrInt(Exception):
    def __init__(self, err_massager):
        self.err_massager = err_massager
q = ""
my_list = []
while q != "q":
    q = input("enter some number or enter 'q' to exit:" )
    if q.lower() == "q":
        break
    else:
        try:
            if q.isdigit():
                my_list.append(int(q))
            else:
                raise ErrInt("\033[31mThe element is not a digit!>20\nthat's why it won't be added to list!\033[0m")
        except ErrInt as err:
            print(err)
print(f"\033[36m final list:\n{my_list}".center(50))