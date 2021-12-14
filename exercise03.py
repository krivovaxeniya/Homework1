class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        sub = self.count - other.count
        return sub if sub > 0 else 'Отрицательное число невозможно'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count / other.count

    def make_order(self, row):
        string = ''
        for i in range(int(self.count / row)):
            string += '*' * row + '\n'
        string += '*' * (self.count % row) + '\n'
        return string

cell_1 = Cell(25)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(9))