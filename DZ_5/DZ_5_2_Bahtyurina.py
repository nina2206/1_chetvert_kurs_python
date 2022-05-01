# Подсчет слов и строк в файле
# числа не считает, только слова (т.е.наборы из букв)
my_fi = open("test.txt", "r", encoding="utf-8")
i = 0
while True:
    one_line = my_fi.readline()
    if not one_line:
        break
    else:
        i += 1
        c_words = [n for n in one_line.split(" ") if n.isdigit() == False and n != "\n"]
        print(f"{i} line - there are {len(c_words)} words")
my_fi.seek(0)
print("Total amount of lines: ", len(my_fi.readlines()))
my_fi.close()
