"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов"""

def my_func(a, b, c):
    result = 0
    try:
        result = a + b + c - min(a, b, c)
    except TypeError:
        print('Неверный формат данных')
    return result


print(my_func(2, -5, 1))