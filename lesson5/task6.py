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
        print(key)
        value = line.split('(')
        print(value)
# print(my_dict)


