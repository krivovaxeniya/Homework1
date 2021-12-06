file = open('for_exercise02.txt', 'r', encoding = 'utf-8')
content = file.read()
print(content)

file = open('for_exercise02.txt', 'r', encoding = 'utf-8')
count_lines = file.readlines()
print(f'Количество строк файла = {len(count_lines)}')

file = open('for_exercise02.txt', 'r', encoding = 'utf-8')
count_lines = file.readlines()
i = 0
for el in count_lines:
    print(f'Длина строки {i + 1} = {len(count_lines[i])}')
    i += 1

file.close()
