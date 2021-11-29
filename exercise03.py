def my_func(num_1, num_2, num_3):
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        num_3 = float(num_3)
        sum_all = num_1 + num_2 + num_3
        summa = sum_all - min(num_1, num_2, num_3)
        return summa
    except ValueError:
        return 'Ошибка типа данных'

print(my_func(num_1 = input('Введите первое число '),
              num_2 = input('Введите второе число '),
              num_3 = input('Введите третье число ')))
