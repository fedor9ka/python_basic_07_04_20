"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
цикл while и арифметические операции"""

number = input('Введите любое положительное число: ')
number = int(number)
i = 0

while number > 9:
    rest = number % 10
    number = number // 10
    if rest > i:
        i = rest
print(i)






