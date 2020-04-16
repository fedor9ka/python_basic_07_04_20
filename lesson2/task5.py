""" Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

while True:
    user_number = input('Введите рейтинг: ')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('Ошибка ввода, это не число')

my_list = [7, 5, 3, 3, 2]
print(my_list)
i = 0
if user_number in my_list:
    index = my_list[::-1].index(user_number)
    index = len(my_list) - index
    my_list.insert(index, user_number)
    print(my_list)
elif user_number < my_list[-1]:
    my_list.append(user_number)
else:
    while my_list[i] >= user_number and i < (len(my_list) - 1):
        i += 1
    my_list.insert(i, user_number)

print(my_list)

