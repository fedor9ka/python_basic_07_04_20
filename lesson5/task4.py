"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

with open('task4.txt', 'r', encoding='UTF-8') as file:
    with open('task4(1).txt', 'w', encoding='UTF-8') as file2:
        my_list = list()
        for line in file.readlines():
            my_list.append(line.split(' '))
        # print(my_list)

        rus_list = ['Один', 'Два', 'Три', 'Четыре']

        j = 0
        for i in my_list:
            i[0] = rus_list[j]
            j += 1
        # print(my_list)

        result = ''
        for param in my_list:
            result += ' '.join(param)
        # print(result)
        file2.writelines(result)
