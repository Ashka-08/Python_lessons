# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, 
# считаем что у нас квадрат.

class Square:

    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return 2 * (self.a + self.b)


sq1 = Square(3, 4)
print(sq1.get_area(), sq1.get_perimetr())

sq2 = Square(3)
print(sq2.get_area(), sq2.get_perimetr())