"""Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input()."""
user_list = []
j = 0
while j < 5:
    itm = input('Введите элемент списка: ')
    user_list.append(itm)
    j += 1
print(user_list)

a = user_list[::2]
b = user_list[1::2]
new_list = []
index = 0

while index < len(b):
    new_list.append(b[index])
    new_list.append(a[index])
    index += 1

if len(user_list) // 2 != 0:
    new_list.append(user_list[-1])

print(new_list)


