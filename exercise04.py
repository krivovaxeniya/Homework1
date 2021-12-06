my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('for_exercise04.txt', 'r', encoding = 'utf-8') as file:
    content = file.read().split('\n')
    print(content)
    data = {}
    for el in content:
        key, value = el.split(' — ')
        data[key] = value
    data_new = []
    for el in data.items():
        data_new.append(my_dict[el[0]] + ' — ' + el[1])
    print(data_new)

with open('for_exercise04_new.txt', 'w', encoding = 'utf-8') as file_new:
    for el in data_new:
        file_new.writelines(el + '\n')
