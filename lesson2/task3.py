"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""
# while True:
#     user_month = input('Введите номер месяца: ')
#     if user_month.isdigit():
#         user_month = int(user_month)
#         if user_month > 0 and user_month <= 12:
#             break
#         else:
#             print('Введите число от 0 до 12')
#     else:
#         print('Ошибка ввода, это не число')
#
# season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
# print(season_list[user_month - 1])

season_dict = {'1': 'зима',
               '2': 'зима',
               }
for key, value in season_dict.items():
    print(f'{key} --- {value}')
