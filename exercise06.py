products = []
prod_units = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'eд': []}
i = 0
while True:
   if input('Добавить товар? y/n ').upper() == 'N':
       break
   i = i + 1
   for p in prod_units.keys():
       prod = input(f'Введите значение поля {p} для товара ')
       prod_units[p] = prod
       analytics[p].append(prod_units[p])
   products.append((i, prod_units.copy()))


choice = input('Введи 1 для просмотра списка товаров, 2 для просмотра аналитики ')
if choice == '1':
    print(*products, sep = '\n')
elif choice == '2':
    for key, value in analytics.items():
        print(f"{key}: {value}")
