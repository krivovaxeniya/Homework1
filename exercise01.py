from sys import argv

work_hours = input('Введите количество отработаных часов: ')
rate_in_hour = input('Введите значение ставки в час: ')
bonus = input('Введите сумму премии: ')

def salary():
    try:
        salary = (float(work_hours) * float(rate_in_hour)) + float(bonus)
        print(f'Ваша зарплата = {salary}')
    except ValueError:
        print( 'Ошибка формата данных! Требуется ввести численные значения')

salary()
