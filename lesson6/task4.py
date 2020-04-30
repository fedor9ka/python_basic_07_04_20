"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed: float, colour: str, name: str, is_police: bool):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car started')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'Car goes {direction}')
        else:
            print("Choose from 'left' or 'right'")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed}Превышение скорости')


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


test_1 = TownCar(speed= 70, colour= 'blue', name= 'KIA', is_police= False)
test_2 = WorkCar(speed= 75, colour= 'red', name= 'Toyota', is_police= False)
test_3 = PoliceCar(speed= 80, colour= 'yellow', name= 'Vaz', is_police= True)

print(1)