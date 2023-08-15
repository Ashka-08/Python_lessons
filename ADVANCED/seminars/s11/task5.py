# Задание №5
# # Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем стороны.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


from functools import total_ordering


@total_ordering
class Square:
    """Класс Прямоугольник.
    Доступны методы сложения, вычитания, определения площади,
    а также сравнения двух прямоугольников по площади"""
    
    def __init__(self, a, b):
        """Создание экземпляра класса Прямоугольник
        :param a: длина стороны а,
        :param b: длина стороны b
        Если a=b, можно передать в метод только длину стороны a"""
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b
            
    def __add__(self, other):
        """Переопределение метода сложения двух прямоугольников"""
        if isinstance(other, Square):
            return Square(self.a + other.a, self.b + other.b)
        return NotImplemented
    
    def __sub__(self, other):
        """Переопределение метода вычитания двух прямоугольников"""
        if isinstance(other, Square):
            if other.a > self.a  or other.b > self.b:
                raise ValueError('Такой прямоугольник невозможен')
            return Square(self.a - other.a, self.b - other.b)
        return NotImplemented

    def get_area(self):
        """Метод вычисления площади прямоугольника"""
        return self.a * self.b

    def get_perimetr(self):
        """Метод вычисления периметра прямоугольника"""
        return 2 * (self.a + self.b)
    
    def __repr__(self):
        """Переопределение метода представления repr класса прямоугольника"""
        return f"Square({self.a}, {self.b})"

    def __str__(self):
        """Переопределение метода строкового представления класса прямоугольника"""
        return f"({self.a}, {self.b})"
    
    def __eq__(self, other):
        """Переопределение метода сравнения двух прямоугольников по площади"""
        if isinstance(other, Square):
            return self.get_area() == other.get_area() 
        return NotImplemented
    
    def __gt__(self, other):
        """Переопределение метода определения большего из 2 прямоугольников по площади"""
        if isinstance(other, Square):
            return self.get_area() > other.get_area()
        return NotImplemented     

    # def ge(self, other):
    #     if isinstance(other, Square):
    #         return self.get_area() >= other.get_area()
    #     return NotImplemented          
       

square_1 = Square(3, 4)
square_2 = Square(5, 6)

square_3 = square_1 + square_2
square_4 = square_2 - square_1

print(f"{square_1} + {square_2} = {square_3}")
print(f"{square_2} - {square_1} = {square_4}")

print(square_1 > square_2)
print(square_1 < square_2)
print(square_1 >= square_2)
print(square_1 <= square_2)
print(square_1 == square_2)
print(square_1 != square_2)