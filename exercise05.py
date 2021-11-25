my_list = [7, 5, 3, 3, 2]
el = int(input('Введите новый элемент списка '))
i = 0
for num in my_list:
    if el <= num:
        i = i + 1
    else:
        break
my_list.insert(i, el)
print(my_list)
