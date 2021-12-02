def fact(n):
    fact = 1
    for el in range(1, n+1):
        fact = fact * el
        yield fact

n = int(input('Введи число n '))
i = 1

while i <= n:
    for el in fact(n):
        print(f'Факториал числа {i} = ', el)
        i += 1
