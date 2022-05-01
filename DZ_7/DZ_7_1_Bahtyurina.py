# Задание 1
# Вывод и сложение матриц
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(["\t".join([str(el) for el in line]) for line in self.matrix])

    def __add__(self, other):
        return Matrix(map(lambda line_s, line_o: map(lambda el_in_line_s, el_in_line_o: el_in_line_o + el_in_line_s,
                                                     line_s, line_o), self.matrix, other.matrix))


matrix_1 = Matrix([[12, 34], [13, 123], [12, 23]])
matrix_2 = Matrix([[122, 334], [1, 12], [126, 23]])

print(matrix_1)
print(matrix_2)
summa = matrix_1 + matrix_2
print(summa)