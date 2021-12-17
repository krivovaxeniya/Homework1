class Office_tech:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            print(item)
        except ValueError:
            print('Недопустимое значение!')

class Printer(Office_tech):
    def print(self):
        print('Это принтер')

class Scaner(Office_tech):
    def scan(self):
        return 'Это сканер'

class Xerox(Office_tech):
    def xer(self):
        return 'Это ксерокс'

prin = Printer('Hp', 4, 3000)
scan = Scaner('Canon', 1, 5000)
x = Xerox('Xerox', 7, 15000)
prin.income()
scan.income()
x.income()