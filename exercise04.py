text = input('Введите несколько слов: ').split()
i = 1
for el in text:
    print(i, el[:10])
    i = i + 1