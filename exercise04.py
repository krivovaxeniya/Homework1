def my_func(x, y):
    try:
       x = float(x)
       y = int(y)
       if x > 0 and y < 0:
          z = (1/x)**abs(y)
          return z
       else:
          return 'Число x должно быть больше 0, y - меньше 0'
    except ValueError:
        return 'Ошибка типа данных'

print(my_func(x = input('Введи число x '),
              y = input('Введи число y ')))
