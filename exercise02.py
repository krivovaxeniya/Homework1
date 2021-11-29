def user(name, surname, year, city, email, phone):
    return print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {year}; Город проживания: {city}; Эл.почта: {email}; Телефон: {phone}')

user(name = input('Введите имя: '),
     surname = input('Введите фамилию: '),
     year = input('Введите год рождения: '),
     city = input('Введите город проживания: '),
     email = input('Введите адрес эл.почты: '),
     phone = input('Введите номер телефона: '))

