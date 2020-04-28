"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('task3.txt', 'r', encoding='UTF-8') as file:
    my_dict = {}
    while True:
        try:
            data = file.readline()
            line = data.split(' ')
            my_dict[line[0]] = line[1].strip()
        except IndexError:
            break
    # print(my_dict)
    for key, value in my_dict.items():
        if float(value) < 20000:
            print(f'{key} имеет оклад менее 20000')
    result = 0
    for i in my_dict.values():
        try:
            result += float(i)
        except ValueError as e:
            print(e)
    average = result / len(my_dict)
    print(f'Средняя зарплата сотрудников составляет {average}')
