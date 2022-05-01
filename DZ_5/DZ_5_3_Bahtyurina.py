# Расчет среднего оклада
# Список сотрудников, с окладами менее 20 000 р.
with open("text_3.txt", "r", encoding="utf-8") as my_fi:
    my_dict = {my_li.split(" ")[0]: float(my_li.split(" ")[1]) for my_li in my_fi}
    print(f"everage salary: {sum(my_dict.values())/len(my_dict):.2f}")
    print(f"loew salary list: {[k for k in my_dict if my_dict[k] < 20000]}\n")