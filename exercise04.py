number = input('Введи целое положительное число ')
i = len(number)
number = int(number)


if number < 0:
    print('Необходимо ввести положительное число ')
else:
    max = number % 10
    while i > 0:
         max_1 = number % 10
         number = number // 10
         i = i - 1
         if max < max_1:
            max = max_1
print(max)
