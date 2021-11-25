my_list = input('Введите несколько чисел: ').split()
print(my_list)
i = 0
for el in my_list:
    if len(my_list) % 2 == 1:
        my_list[:-1:2], my_list [1::2] = my_list[1::2], my_list [:-1:2]
    else:
       while i + 2 <= len(my_list):
          my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
          i = i + 2
print(my_list)
