"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint

numbers = [randint(-100, 100) for i in range(20)]
print(sum(numbers))


with open('task5.txt', 'w', encoding='UTF-8') as file:
    my_str = ' '.join(map(str, numbers))
    # print(my_str)
    file.writelines(my_str)

with open('task5.txt', 'r', encoding='UTF-8') as file2:
    numbers_1 = map(float, file2.readline().split(' '))
print(sum(numbers_1))
print(sum(numbers_1))

assert sum(numbers_1) == sum(numbers), 'Сработал Assert'