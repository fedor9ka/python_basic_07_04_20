""""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
 данных о пользователе одной строкой."""

result = {}
def data(*kwargs):
    result['name'] = input('Введите имя: ')
    result['surname'] = input('Введите фамилия: ')
    result['birth'] = input('Введите год рождения: ')
    result['city'] = input('Введите город проживания: ')
    result['email'] = input('Введите email: ')
    result['cell'] = input('Введите телефон: ')
    for key, value in result.items():
        print(f'{key} --- {value},', end=' ')


data()