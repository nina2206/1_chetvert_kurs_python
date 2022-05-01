# Задания 6 и 7
# Обработка текста
# Вариант 1
def int_func(t):
    """Возвращает слово с заглавной буквы
    обрабатывает только слова из строчных латинских букв
    оставляет как есть слова, содержащие символы, цифры, кирилицу, заглавную латиницу
    """
    for i in list(t):
        if t.isalpha() and 96 < (ord(i)) < 123:
            return t.title()
        else:
            return t


print (int_func(input("ваше слово: ")))
fraza = input("введите фразу: ").split(" ")
for i in fraza:
    print(int_func(i), "", end="")

