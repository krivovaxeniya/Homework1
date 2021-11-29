def text():
    while True:
        texts = input('Введите несколько слов: ')
        for i in texts:
            if i in ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
                     'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                     'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
                texts = texts.title()
                return texts
            else:
                return 'Требуется ввести слово из латинских букв'
print(text())
