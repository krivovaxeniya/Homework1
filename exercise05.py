def file_sum():
    try:
        with open('for_exercise05.txt', 'w', encoding = 'utf-8') as file_write:
            numbers = input('Введите несколько чисел ')
            file_write.write(numbers)
            numbers = numbers.split()
            print(sum(int(el) for el in numbers))
    except ValueError:
        print('Необходимо ввести числа')

file_sum()