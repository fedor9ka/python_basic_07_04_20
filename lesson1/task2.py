"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк"""

seconds = input('Введите количество секунд: ')

if seconds.isdigit():
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds - hours * 3600 - minutes * 60

    print(f'{hours:>02}:{minutes:>02}:{seconds:>02}')

else:
    print('Неверный формат')



