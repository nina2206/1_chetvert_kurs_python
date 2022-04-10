# Задание 4
# поиск самой большой цифы
some_num = input("Введите любое число: ")
bigest = 0
for dig in some_num[::1]:
    if dig == "." or dig == ",":
        continue
    elif bigest < int(dig):
        bigest = int(dig)

print (f"самая большая цифра в числе {some_num} - цифра {bigest}")
       