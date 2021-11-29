def div():
    divisible = float(input('Введите делимое '))
    divisor = float(input('Введите делитель '))
    if divisor == 0:
        print('Ошибка! На ноль делить нельзя')
    else:
        quot = divisible / divisor
        return quot
quotient = div()
print(quotient)