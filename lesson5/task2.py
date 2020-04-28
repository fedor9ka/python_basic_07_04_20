"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('text.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()
    line_amount = len(data)
    print(f'Количество строк: {line_amount}')
    j = 1
    for i in data:
        words_amount = len(i.split(' '))
        print(f'В {j} строке {words_amount} слов')
        j += 1