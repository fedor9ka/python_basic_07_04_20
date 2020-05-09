from abc import ABC, abstractmethod
import time
from lesson6.les6 import HomoSap


def step(self, any: int) -> None:
    print(self.name)
    print('STEPS', any)


setattr(HomoSap, 'step', step)


class MyInterface(ABC):

    @property #2) хватает wrap и подменяет его своим враппером
    @abstractmethod #1) в него передается функция name, он возвращает подмененную функцию wrap
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self, x: int, y:int) -> float:
        pass

    @abstractmethod
    def turn_off(self, x: int) -> None:
        pass

    def say(self): #создали не абстрактный метод и его уже не нужно описывать в MyCls
        print(self.name)


class ClsIter: #это итератор класс изменный. логика итератора for, можно изменить, взатмодействует с def __iter__
    def __init__(self, name, x):
        self.name = name
        self.x = x

    def __next__(self): # итератор не просто организует проход по объекту, можно сделать сколь угодно сложный итератор,
        if self.x != 0: #объединяя различные объекты например
            result = self.name[self.x] if len(self.name) > self.x else self.name[0]
            self.x -= 1
            return result
        raise StopIteration # вызываем ошибку, срабатывает завершение цикла


class MyCls(MyInterface):

    def __init__(self, name):
        self.one = '22222'
        self.__name = name
        self.name2 = ''
        self.i = 4

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        print(data)
        self.name2 = data

    def turn_on(self, x: int, y: int) -> float:
        return x / y

    def turn_off(self, x: int) -> None:
        print('Hello', x)

    def __str__(self):
        return self.__name

    def __add__(self, other):
        return MyCls(self.name.split(' ')[0] + other.name.split(' ')[-1])

    def __eq__(self, other):
        return self.__name == other.name

    def __call__(self, x, y):
        tmp = x ** y
        return f'{self.__name} -- {tmp}'

    def __iter__(self):
        return ClsIter(self.name, 55)
        #self.i = 4 это если используем итератор внутри класса, который описан ниже
        #return self

    def __next__(self): #это итератор внутри класса, работает в рамках одного объекта
        if self.i:
            result = self.i **2
            self.i -= 1
            return result
        raise StopIteration




def my_deco(func):
    def wrap(*args, **kwargs):
        print(func.__name__, time.time())
        tmp = func(*args, **kwargs)
        print('end')
        return f'<p>{tmp}</p>' #мы изменили поведение нашей функции test1

    return wrap


@my_deco
def test1(text):
    print(text)
    return f'<span>{text}</span>'


@my_deco
def test2():
    print('TEST2')


if __name__ == '__main__':
    tmp = MyCls('Some Name')
    tmp_1 = MyCls('Some Name')
    tmp2 = MyCls('Name @2New')
    tmp3 = tmp + tmp2 #эквивалент tmp3 = tmp.__add__(tmp2)
    some = 'Some STR'
    some = tmp(5, 2)

    homo = HomoSap(colour= 'Green', name= 'Joe')
    homo2 = HomoSap(colour='RED', name='Bill')

    print(tmp)
    print(tmp3)
    print(tmp == tmp_1)
    print(some)

    tmp_iter = tmp.__iter__()
    for itm in tmp:
        print(itm)

    # tmp.name = 'New name'
    #
    # print(tmp.name)
    # print(tmp.name2)
    # test1 = my_deco(test1)
    # print(test1('Some text'))
    print(1)



