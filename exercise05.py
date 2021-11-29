def summa():
  sum = 0
  while True:
      numbers = input('Введите несколько чисел или n для выхода: ').split()
      for num in numbers:
          if num == 'n':
             return sum
          else:
              try:
                  sum += int(num)
              except ValueError:
                  return 'Ошибка формата данных'
      print(f'Сумма чисел = {sum}')
print(summa())