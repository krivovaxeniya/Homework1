income = int(input('Введите сумму выручки Вашей фирмы '))
loss = int(input('Введите сумму издержек Вашей фирмы '))
profit = income - loss

if income > loss:
    count = int(input('Введите количество сотрудников фирмы '))
    rent = profit / income
    profit_1 = profit / count
    print('Поздравляю! Вы в прибыли, дела идут хорошо')
    print('Рентабельность выручки = ', rent)
    print('Прибыль на одного сотрудника = ', profit_1)
elif income < loss:
    print('Печально, но Вы в убытке')
else:
    print('Вышли в ноль')
