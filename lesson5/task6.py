"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран."""


my_dict = {}
with open('task6.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        data = line.split(' ')
        # print(data)
        key = data[0].split(':')[0]
        my_dict[key] = data[1:]

print(my_dict)
new_dict = {}
for key, value in my_dict.items(): #Информатика ['', '', '100(л)', '', '', '50(пр)', '', '', '20(лаб)\n']
    result = 0
    for i in value:
        if i.split('(')[0].isdigit():
            result += int(i.split('(')[0])
        else:
            continue
    # print(result)
    new_dict[key] = result

print(new_dict)



