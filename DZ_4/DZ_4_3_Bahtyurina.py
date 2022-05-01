#Задание 3
# Список чисел , кратных 20 или 21

new_list = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(new_list)