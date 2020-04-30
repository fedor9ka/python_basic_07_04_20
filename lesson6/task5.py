"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра."""


class Stationery:
    title = 'Заголовок'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        print('Запуск отрисовки маркером')

tmp = Stationery()
tmp_1 = Pen()
tmp_2 = Pencil()
tmp_3 = Handle()

tmp.draw()
tmp_1.draw()
tmp_2.draw()
tmp_3.draw()