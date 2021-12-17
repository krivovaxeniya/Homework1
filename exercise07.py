class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение чисел = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'

z_1 = Complex(1, -2)
z_2 = Complex(2, 1)
print(z_1 + z_2)
print(z_1 * z_2)
