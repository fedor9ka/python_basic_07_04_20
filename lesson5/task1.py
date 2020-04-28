"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка."""

with open('text.txt', 'w', encoding='UTF-8') as fail:
    while True:
        message = input('Введите данные для записи: ')
        if message:
            fail.writelines(f'{message}\n')
        else:
            break

