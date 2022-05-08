#Задание 7
# Операции с комплексными числами
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a, self.b * other.b)

    def __str__(self):
        return ("+".join(map(str, [self.a, self.b])) + "j")

a = Complex(3, 4)
b = Complex(3, 10)
c = Complex(1, 3)

print(f"1-st complex number: {a}\t 2-th complex number: {b}\t 3-th complex number: {c}")
print(f"Addition: {a + b + c}")
print(f"Multiplication: {a * b * c}")
