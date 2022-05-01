#Расчет финансового результата
#Сериализация: вывод в json-файл
import json
with open("text_77.json", "w", encoding="utf-8") as my_fi_j, open("text_7.txt", "r", encoding="utf-8") as my_fi_t:
    fin_res = {my_li.split()[0]: int(my_li.split()[2]) - int(my_li.split()[3]) for my_li in my_fi_t}
    everage_profit = [el for el in fin_res.values() if el > 0]
    total_list = [fin_res, {"Everage profit": sum(everage_profit) / len(everage_profit)}]
    json.dump(total_list, my_fi_j, ensure_ascii=False, indent="\t", sort_keys=True)

