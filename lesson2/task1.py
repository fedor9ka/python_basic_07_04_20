""" Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе."""

new_list = ['строка', 258, 0, None, ['нечто', True], False]
for i in new_list:
    print(i, type(i))