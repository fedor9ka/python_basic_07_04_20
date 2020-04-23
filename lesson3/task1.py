""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль"""


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def division():
    while True:
        a = input('Введите число a: ')
        b = input('Введите число b: ')
        if is_number(a) and is_number(b):
            try:
                result = float(a) / float(b)
                return print(result)
            except ZeroDivisionError as e:
                print(f'{e}\nДеление на 0 запрещено')
        else:
            print('Неверный формат данных')


division()


