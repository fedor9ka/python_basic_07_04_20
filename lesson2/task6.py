"""6)	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}"""
while True:
    user_number = input('Введите количество позиций товаров: ')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print('Ошибка ввода, это не число')

i = 0
my_list = []
while i < user_number:
    my_dict = {}
    my_tuple = ()
    user_item = input('Введите название товара: ')
    my_dict['название'] = user_item
    user_price = input('Введите цену товара: ')
    if user_price.isdigit():
        user_price = int(user_price)

    else:
        print('Ошибка ввода, это не число')
    my_dict['цена'] = user_price
    user_amount = input('Введите количество товара: ')
    if user_amount.isdigit():
        user_amount = int(user_amount)
    else:
        print('Ошибка ввода, это не число')
    my_dict['количество'] = user_amount
    user_unit = input('Введите единицу измерения товара: ')
    my_dict['eд'] = user_unit
    my_tuple = (i+1, my_dict)
    my_list.append(my_tuple)
    i += 1

for itm in my_list: print(itm)


print(my_list[0][1].get('название'))
i = 0

item = []
price = []
amount = []
unit = []
while i < user_number:
    item.append(my_list[i][1].get('название'))
    price.append(my_list[i][1].get('цена'))
    amount.append(my_list[i][1].get('количество'))
    unit.append(my_list[i][1].get('eд'))
    i += 1


result = {}
result['название'] = item
result['цена'] = price
result['количество'] = amount
result['eд'] = set(unit)

print(result)






