"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.

"""

from copy import deepcopy

# class Matrix:
#
#     def __init__(self, data: list):
#         self.__data = deepcopy(data) # создает копию - новый объект
#         self.__shape = (len(max(self.__data, key = len)), len(self.__data)) # кортеж, в котором указываем размерность матриц
# # len(max(self.__data, key = len)) ширина матрицы - это если разной длины списки, то берем макс, len(self.__data) - высота
#         if len(min(self.__data, key = len)) != self.__shape[0]: # если списки разной длины, мы заполняем пустоты нулями
#             return self.__reshape()



    # def __str__(self):
    #     return self.data




matrix = [[5, 3], [1, 4], [7, 5, 9]]
print(len(max(matrix, key = len)))

print(1)