from random import randint
my_list = []
i = 0
while i < 10:
    el = randint(0, 1000)
    my_list.append(el)
    i += 1
print(my_list)

my_list_biggest = [my_list[j + 1] for j in range(0, len(my_list)-1) if my_list[j] < my_list[j+1]]
print(my_list_biggest)
