from itertools import count, cycle
my_list_1 = []
i = 1
for el in count(3):
    if el < 10:
        my_list_1.append(el)
    else:
        break
print(my_list_1)

my_list_2 = []
i = 0
for el in cycle(my_list_1):
    if i < len(my_list_1)*3:
        my_list_2.append(el)
        i += 1
    else:
        break
print(my_list_2)
