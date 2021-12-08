class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Сотрудник: {full_name}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход сотрудника с учетом премии: {total_income}')

a = Position(input('Введи имя '), input('Введи фамилию '), input('Введи должность '), input('Введи размер зп '), input('Введи размер премии '))
a.get_full_name()
a.get_total_income()
