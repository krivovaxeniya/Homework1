first_day = int(input('Укажи кол-во км в 1-й день '))
wish_day = int(input('Укажи желаемое кол-во км '))
day = 1

while first_day <= wish_day:
    first_day = 1.1 * first_day
    day = day + 1

print('На ', day, 'день спортсмен достиг результата - не менее', wish_day, 'км')
