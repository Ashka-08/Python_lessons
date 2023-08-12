# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi*self.radius**2

    def get_perimetr(self):
        return 2*pi*self.radius

radius = 1
circle = Circle(radius)
print(f"{circle.get_area()}, {circle.get_perimetr()}")