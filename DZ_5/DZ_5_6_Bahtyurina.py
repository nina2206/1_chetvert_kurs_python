#подсчет количества занятий по предметам
import re
with open("text_6.txt", "r", encoding="utf-8") as my_fi:
     my_dict = {my_li.split(":")[0]: sum(int(i) for i in re.split(r"\D", my_li.split(":")[1]) if i.isdigit()) for my_li in my_fi}
print(f"{'Предмет':<15}: {'Всего уроков':<5}")
for el in my_dict.items():
    print(f"{el[0]:<15}: {el[1]:<5}")