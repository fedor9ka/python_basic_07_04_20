import random
import time


class Wolf:
    _proto = True

    def __init__(self, eye):
        self.eye = eye


    def moon(self):
        print('UUUUUUUUUUUUUUUU')

    def ask(self):
        print('RRRRRR')


class Homo(object):
    age = 0
    sex = random.choice(('m', 'f'))
    weight = 3400
    population = 0


    def __init__(self, name: str):
        # self.surname = surname
        self.name = name
        Homo.population += 1

    def ask(self):
        print(f'my name is {self.name}')

    def new_age(self):
        self.age += 1

    def get_population(self):
        return self.population

class HomoSap(Homo):

    def __init__(self, colour, *args, **kwargs):
        self.colour = colour
        super().__init__(*args, **kwargs)


class WereWolf(HomoSap, Wolf):

    age = 1 #переопределили атрибут
    _proto = False

    def __init__(self, colour, eye, *args, **kwargs):
        super().__init__(colour, *args, **kwargs) #HomoSap.__init__(self, colour, *args, **kwargs)
        Wolf.__init__(self, eye)

    def ask(self): #переопредлили поведение ask в зависимости от времени, можно задать и переменную, но это
        # не хорошо, если метод который раньше ничего не принмал - начал принимать аргументы. Мы изменяем лишь поведение
        # этого свойства
        # print(var_test)
        now = int(time.time())
        if now & 1:
            #self.moon() например нам нужно иногда дергать метод ask y Homo, а иногда у Wolf
            Wolf.ask(self)
        else:
            #print('Who i am')
            super().ask()
#
# vasya = Homo(name='Вася')
# petya = Homo(name='Петя')

new_vasya = HomoSap('red', name='New_vasya')
wr = WereWolf(colour='Gray', eye= 'Green', name='Joe')
# wr.ask('Hello')

print(Homo.population)