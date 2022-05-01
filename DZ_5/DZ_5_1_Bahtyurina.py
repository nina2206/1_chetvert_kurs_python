# Создание файла (програмно) / либо откроет на запись, если файл ранее был создан

with open("test.txt", "w", encoding="utf-8") as my_fi:
    i = 0
    while True:
        i += 1
        my_li = input(f'Line {i}: ')
        my_fi.writelines(f"{my_li}, \n")
        if my_li == "":
            break
if my_fi.closed:
    print(f"Data recording {my_fi.name} was complete")