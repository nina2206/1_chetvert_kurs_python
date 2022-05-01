# Перевод слов (работает не зависимо от положения переводимого слова в строке, регистрочувствительный переводчик)
rus_dict = {"One": "Oдин", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}
with open("Text_4.txt", "r", encoding="utf-8") as my_fi:
    for li in my_fi:
        f = 0
        for el in rus_dict.items():
            if li.find(el[0]) != -1:
                li = li.replace(el[0], el[1])
                f += 1
        if f > 0:
            print(f"{li}", end="")
        else:
            print(f"{li} (no element in user's dictionary)", end="")

