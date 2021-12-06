import json
list = []
plus_dict = {}
avg_dict = {}
minus_dict = {}
sum_prof = 0
count = 0
with open('for_exercise07.txt', 'r', encoding = 'utf-8') as file_write:
    for line in file_write:
        name, form, income, minus = line.split()
        profit = int(income) - int(minus)
        if profit > 0:
            plus_dict[name] = profit
            sum_prof += profit
            count += 1
        else:
            minus_dict[name] = profit
        avg_profit = sum_prof / count
        avg_dict['average_profit'] = avg_profit
    list.append(plus_dict)
    list.append(avg_dict)
    list.append(minus_dict)

print(list)

with open("for_exercise07.json", "w") as write_json:
    json.dump(list, write_json)