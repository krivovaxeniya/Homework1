class Only_number:
    def __init__(self):
        pass

    @staticmethod
    def numbers():
        my_list_nums = []
        while True:
            my_list = input('Введите числовые значения ').split()
            for el in my_list:
                try:
                    my_list_nums.append(int(el))
                except ValueError:
                    print(f'Недопустимое значение {el}')
            ex = input(f'Список = {my_list_nums}. Для выхода нажмите n, либо Enter для продолжения ')
            if ex == 'n':
                print(f'Ваш список: {my_list_nums}')
                break

Only_number.numbers()

