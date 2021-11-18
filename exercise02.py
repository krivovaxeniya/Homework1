import datetime, time
second = int(input('Введи количество секунд '))
hour = second // 3600
ostatok = second % 3600
min = ostatok // 60
sec = ostatok % 60
time = datetime.time(hour, min, sec)
print(time)
