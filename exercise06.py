subj_dict = {}
with open('for_exercise06.txt', 'r', encoding = 'utf-8') as file_write:
    for line in file_write:
        subj, inf = line.split(':')
        numbers = [el for el in inf if el in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ')]
        hours = (''.join(numbers)).split()
        hours_int = [int(el) for el in hours]
        summa = sum(hours_int)
        subj_dict[subj] = summa

print(subj_dict)

