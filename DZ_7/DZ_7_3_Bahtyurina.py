# Задание 3
# Операции с клетками

class Cells:
    def __init__(self, el):
       self.struct = el

    def __add__(self, other):
        return Cells(self.struct + other.struct)

    def __sub__(self, other):
        if abs(self.struct - other.struct) !=0:
            return Cells(abs(self.struct - other.struct))
        else:
            return "Zero rusult. Cells are just the same"

    def __mul__(self, other):
        return Cells(self.struct * other.struct)

    def __truediv__(self, other):
        if (self.struct // other.struct) >= 1:
            return Cells(self.struct // other.struct)
        else:
            return Cells(other.struct // self.struct)

    def make_order(self, els_in_row):
        return "\n".join([' * ' * els_in_row for _ in range(self.struct // els_in_row)]) +\
               '\n' + ' * ' * (self.struct % els_in_row) + '   ' * (els_in_row - self.struct % els_in_row)

    def __str__(self):
        return f"{self.struct}"


cell_1 = Cells(10)
cell_2 = Cells(12)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
# Выводит исходные массивы клеток и результаты вычислений в виде графических матриц
print(f"First matrix:\n{cell_1.make_order(3)}\n")
print(f"Second matrix:\n{cell_2.make_order(6)}\n")
print(f"Matrix cell_1 + cell_2: \n{(cell_1 + cell_2).make_order(5)}\n")
print(f"Matrix cell_1 * cell_2: \n{(cell_1 * cell_2).make_order(5)}\n")
print(f"Matrix cell's devision: \n{(cell_1 / cell_2).make_order(5)}\n")
print(f"Matrix cell's subrtaction: \n{(cell_1 / cell_2).make_order(5)}\n")