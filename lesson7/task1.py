"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.

"""

from copy import deepcopy


class Matrix:
    def __init__(self, data: list):
        self.__data = deepcopy(data) # создает копию - новый объект, абсолютный клон
        self.__shape = (len(max(self.__data, key=len)), len(self.__data)) # кортеж, в котором указываем размерность матриц
# len(max(self.__data, key = len)) ширина матрицы - это если разной длины списки, то берем макс, len(self.__data) - высота
        if len(min(self.__data, key=len)) != self.shape[0]: # если списки разной длины, мы заполняем пустоты нулями
            self.__reshape()

    @property
    def shape(self): # shape у нас величина зивисимая от матрицы, мы еесделали защищенной поэтому
        return self.__shape # изменять извне ее нельзя, но нам нужно знать ее значение, поэтому @property

    def __reshape(self): # заполняем пустоты нолями, в случае, если длина матриц разная, тоже приватный, извне
        for itm in self.__data: # его лучше не запускать
            tmp = self.shape[0] - len(itm)
            if tmp:
                itm.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return self.__data[item]

    def __iter__(self):
        return self.__data.__iter__()

    def __add__(self, other): # отвечает за сложение, other - это матрица
        if not isinstance(other, Matrix): # если поступает не класс матрицы - возбуждаем ошибку
            raise ValueError(f'This is not Matrix, this is {type(other).__name__}')
        if self.shape != other.shape: # спрашиваем self.shape присложении равен other, если нет мы не можем сложить
            raise ValueError(f'Not equal shape matrix {self.shape} and {other.shape}') # то есть если разная рамерность матриц

        return Matrix(list(map(lambda y: list(map(sum, y)), # сложение матриц поэдлементно и создание их сразу
                               map(lambda x: list(zip(*x)), zip(self, other)) # итерируемый объект zip находится в map, мы делаем кортежи из внутренних кортежей
                               # дальше верхнеуровневый map, для которго внтренний map уже является итерируемым объектом
                               ) # благодаря тому, что мы определили итераторы, мы можем обращаться теперь как к self и other
                           )
                      )

    def __str__(self): #  мы вычисляем максимальную длину подстроки от элемнта матрицы
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.__data))))
        if not max_len_itm & 1: # если максимальная длина строки четная, то нельзя будет выровнять по центру
            max_len_itm += 1 # поэтому делаем все нечетными

        result = ''
        for line in self.__data: # чтобы вывод был по колонкам ровным
            result += ''.join([f'{itm:<{max_len_itm}}' for itm in line]) + '\n' # чтобы выравнивать если вместо > будет ^, то по центру
        return result


a = Matrix([[1, 2323], [4, 5], [3, 9, 12]])
b = Matrix([[1, 2323233], [4, 5], [3, 9, 10]])
c = Matrix([[3, 9], [7, 8], [4, 5, 777]])


d = c + b
print(d)
# #
#
# matrix = [[5, 3], [1, 4], [7, 5, 9]]
# print(len(max(matrix, key = len)))
#
# print(1)
