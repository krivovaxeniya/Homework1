with open('for_exercise01.txt', 'w') as file:
    while True:
        line = input('Введи данные ')
        file.write(f'{line}\n')
        if not line:
            break
