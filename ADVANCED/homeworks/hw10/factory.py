# Доработаем задачи 5-6. Создайте класс-фабрику.
# * Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# * Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:

    def __init__(self, name, age, voice = 'groal'):
        self.name = name
        self.age = age
        self.voice = voice
    
    def say(self):
        print(self.voice)


class Fish(Animal):

    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)      
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)  
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name
    
    def fly_around_corpse(self):
        print('oooh, meat....')

class Factory:

    def __new__(self, cls, *args):
        return cls(*args)


fish = Factory(Fish, 'Nemo', 2, 'silver', 'bul-bul')
dog = Factory(Dog, 'Spark', 5, 'pitbull', 'bark!')
bird = Factory(Raven, 'Qarasique', 6, 'white', 'bravo!')

animals = [fish, dog, bird]

for i in animals:
    i.say()