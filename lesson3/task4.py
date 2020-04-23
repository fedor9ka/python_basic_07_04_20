"""Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x: float, y: int):
    result = x ** y if x > 0 and type(y) is int and y < 0 else False
    print(result)


def my_func1(x: float, y: int):
    result = 1
    if x > 0 and type(y) is int and y < 0:
        for i in range(abs(y)):
            result *= x
        return 1/ result
    else:
        False


my_func(2, 3)
my_func(0, -2)
my_func(-1, -2)
my_func(2, 2.5)
my_func(2, -2.2)
my_func(2, -3)

print(my_func1(2, 3))
print(my_func1(0, -2))
print(my_func1(-1, -2))
print(my_func1(2, 2.5))
print(my_func1(2, -2.2))
print(my_func1(2, -3))