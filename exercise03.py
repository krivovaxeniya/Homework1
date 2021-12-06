with open('for_exercise03.txt', 'r', encoding = 'utf-8') as file:
    data = {el.split()[0]: int(el.split()[1]) for el in file}
    print('Список сотрудников с зп меньше 20 тыс:')
    for el in data.items():
        if el[1] < 20000:
            print(el[0])
    print(f'Средняя зарплата = {sum(data.values())/len(data)}')
