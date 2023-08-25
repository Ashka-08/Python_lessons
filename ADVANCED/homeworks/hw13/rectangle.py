from functools import total_ordering
from error import UserNegativeSideRectangleError, UserEqualsClassesError

@total_ordering
class Rectangle:
    """Класс Прямоугольник.
    Доступны методы сложения, вычитания, определения площади,
    а также сравнения двух прямоугольников по площади"""
    
    def __init__(self, a, b):
        """Создание экземпляра класса Прямоугольник
        :param a: длина стороны а,
        :param b: длина стороны b
        Если a=b, можно передать в метод только длину стороны a"""
        if a < 0:
            raise UserNegativeSideRectangleError(a)
        if b < 0:
            raise UserNegativeSideRectangleError(b)
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b
        
    def __add__(self, other):
        """Переопределение метода сложения двух прямоугольников"""
        if not isinstance(other, Rectangle):
            raise UserEqualsClassesError(f'{type(other) =}')
        return Rectangle(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        """Переопределение метода вычитания двух прямоугольников"""
        if not isinstance(other, Rectangle):
            raise UserEqualsClassesError(f'{type(other) =}')
        if other.a > self.a:
            raise UserNegativeSideRectangleError(f'{other.a - self.a}')
        if other.b > self.b:
            raise UserNegativeSideRectangleError(f'{other.b - self.b}')
        return Rectangle(self.a - other.a, self.b - other.b)

    def get_area(self):
        """Метод вычисления площади прямоугольника"""
        return self.a * self.b

    def get_perimetr(self):
        """Метод вычисления периметра прямоугольника"""
        return 2 * (self.a + self.b)
    
    def __repr__(self):
        """Переопределение метода представления repr класса прямоугольника"""
        return f"Rectangle({self.a}, {self.b})"

    def __str__(self):
        """Переопределение метода строкового представления класса прямоугольника"""
        return f"({self.a}, {self.b})"
    
    def __eq__(self, other):
        """Переопределение метода сравнения двух прямоугольников по площади"""
        if not isinstance(other, Rectangle):
            raise UserEqualsClassesError(f'{type(other) =}')
        return self.get_area() == other.get_area() 
    
    def __gt__(self, other):
        """Переопределение метода определения большего из 2 прямоугольников по площади"""
        if not isinstance(other, Rectangle):
            raise UserEqualsClassesError(f'{type(other) =}')
        return self.get_area() > other.get_area()            
       

r1 = Rectangle(-3, 4)
# UserNegativeSideRectangleError: Нельза создать прямоугольник со сторонами отрицательной длины!   
# Ошибка здесь: -3

r2 = Rectangle(3,4)
r3 = (3,4)
print(r2 - r3)
# UserEqualsClassesError: Объекты должны быть экземплярами одного класса! 
# Ошибка здесь: type(other) =<class 'tuple'>