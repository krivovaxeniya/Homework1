year_list = [[0, 'Фиктивный элемент'],
        [1, 'Январь'],
        [2, 'Февраль'],
        [3, 'Март'],
        [4, 'Апрель'],
        [5, 'Май'],
        [6, 'Июнь'],
        [7, 'Июль'],
        [8, 'Август'],
        [9, 'Сентябрь'],
        [10, 'Октябрь'],
        [11, 'Ноябрь'],
        [12, 'Декабрь']]
number = int(input('Введи число от 1 до 12 '))
if number < 1 or number > 12:
    print('Введенное число должно быть в диапазоне от 1 до 12')
elif number in (1, 2, 12):
    print(year_list[number][1], 'Время года - зима')
elif number in (3, 4, 5):
    print(year_list[number][1], 'Актриса весна')
elif number in (6, 7, 8):
    print(year_list[number][1], 'Лееето, ах, лееето')
else:
    print(year_list[number][1], 'Что такое осень?')


year_dict = [{'num': 0, 'name': 'Фиктивный элемент'},
             {'num': 1, 'name': 'Январь'},
             {'num': 2, 'name': 'Февраль'},
             {'num': 3, 'name': 'Март'},
             {'num': 4, 'name': 'Апрель'},
             {'num': 5, 'name': 'Май'},
             {'num': 6, 'name': 'Июнь'},
             {'num': 7, 'name': 'Июль'},
             {'num': 8, 'name': 'Август'},
             {'num': 9, 'name': 'Сентябрь'},
             {'num': 10, 'name': 'Октябрь'},
             {'num': 11, 'name': 'Ноябрь'},
             {'num': 12, 'name': 'Декабрь'}]
number = int(input('Введи число от 1 до 12 '))
if number < 1 or number > 12:
    print('Введенное число должно быть в диапазоне от 1 до 12')
elif number in (1, 2, 12):
    print(year_dict[number]['name'], 'Время года - зима')
elif number in (3, 4, 5):
    print(year_dict[number]['name'], 'Актриса весна')
elif number in (6, 7, 8):
    print(year_dict[number]['name'], 'Лееето, ах, лееето')
else:
    print(year_dict[number]['name'], 'Что такое осень?')
