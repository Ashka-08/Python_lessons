# Создание экземпляра класса, __init__

class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальных задач
        print(f'Создал {self} со свойствами:\n'
            f'{self.name = },\t{self.equipment = },\t{self.life = }')

print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
print('Создаём третий раз')
u_3 = User(equipment=['ловушка', 'прибор ночного видения'],
name='Стэнц')
"""
Создаём первый раз
Создал <__main__.User object at 0x00000271C36F17D0> со свойствами:
self.name = 'Спенглер', self.equipment = [],    self.life = 3
Создаём второй раз
Создал <__main__.User object at 0x00000271C36F1490> со свойствами:
self.name = 'Венкман',  self.equipment = ['протонный ускоритель', 'ловушка'],   self.life = 3
Создаём третий раз
Создал <__main__.User object at 0x00000271C36F30D0> со свойствами:
self.name = 'Стэнц',    self.equipment = ['ловушка', 'прибор ночного видения'], self.life = 3"""
print()


# Контроль создания класса через __new__

class User:

    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance

print('Создаём первый раз')
u_1 = User('Спенглер')
print('Создаём второй раз')
u_2 = User('Венкман')
print('Создаём третий раз')
u_3 = User(name='Стэнц')
"""
Создаём первый раз
Создал класс <class '__main__.User'>
Создал self.name = 'Спенглер'
Создаём второй раз
Создал класс <class '__main__.User'>
Создал self.name = 'Венкман'
Создаём третий раз
Создал класс <class '__main__.User'>
Создал self.name = 'Стэнц'"""
print()


# Расширение неизменяемых классов

class NamedInt(int):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance

print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')
"""
Создаём первый раз
Создал класс <class '__main__.NamedInt'>
Создаём второй раз
Создал класс <class '__main__.NamedInt'>
a = 42  a.name = 'Главный ответ жизни, Вселенной и вообще'      type(a) = <class '__main__.NamedInt'>
b = 73  b.name = 'Лучшее просто число'  type(b) = <class '__main__.NamedInt'>
c = 115 type(c) = <class 'int'>"""
print()

# Шаблон Одиночка, Singleton

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name

a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')
"""
a.name = 'Первый'
a is b = True
a.name = 'Второй'
b.name = 'Второй'"""
print()

# Удаление экземпляра класса, __del__

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')
    def __del__(self):
        print(f'Удаление экземпляра {self.name}')

u_1 = User('Спенглер')
u_2 = User('Венкман')
"""
Создал self.name = 'Спенглер'
Создал self.name = 'Венкман'
Удаление экземпляра Спенглер
Удаление экземпляра Венкман"""
print()


# Команда del

import sys

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')
    def __del__(self):
        print(f'Удаление экземпляра {self.name}')

u_1 = User('Спенглер')
print(sys.getrefcount(u_1))
u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
del u_2
print('Завершение работы')
"""
Создал self.name = 'Спенглер'
Удаление экземпляра Спенглер
2
Удаление экземпляра Венкман
3 3
2
Удаление экземпляра Спенглер
Завершение работы"""
print()


# Задание (класс тройняшки)

class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name


# Строка документации

class User:
    """A User training class for demonstrating class documentation.
    Shows the operation of the help(cls) and the dander method __doc__"""

    def __init__(self, name: str):
        """Added the name parameter.""" # лишняя документация
        self.name = name

    def simple_method(self):
        """Example of a simple method.""" # желательно указывать ко всем недандер методам
        self.name.capitalize()

# u_1 = User('Спенглер')
# print('Справка класса User ниже', '*' * 50)
# help(User)
# print('Справка экземпляра u_1 ниже', '*' * 50)
# help(u_1)


# Хранение документации в __doc__

u_1 = User('Спенглер')
print(f'Документация класса: {User.__doc__ = }')
print(f'Документация экземпляра: {u_1.__doc__ = }')
print(f'Документация метода: {u_1.simple_method.__doc__}')


# Задание

class MyClass:
    A = 42
    """About class"""
    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b
    def method(self):
        """Documentation"""
        self.__doc__ = None

# help(MyClass)


# Представления экземпляра

user = User('Спенглер')
print(user) #<__main__.User object at 0x0000019FF958CFD0>


# Представление для пользователя, __str__

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()
    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'

user = User('Спенглер')
print(user) #Экземпляр класса User с именем "Спенглер"


# Представление для создания экземпляра, __repr__

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()
    def __repr__(self):
        return f'User({self.name})'

user = User('Спенглер')
print(user) #User(Спенглер)
print()


# Еще пример

class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
    def __repr__(self):
        return f'User({self.name}, {self.equipment})'

user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user) #User(Венкман, ['протонный ускоритель', 'ловушка'])


# Приоритет методов

class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
    def __repr__(self):
        return f'User({self.name}, {self.equipment})'

user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user) 
# Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество жизней - 3
print(f'{user}')
# Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество жизней - 3
print(repr(user))
# User(Венкман, ['протонный ускоритель', 'ловушка'])
print(f'{user = }')
# user = User(Венкман, ['протонный ускоритель', 'ловушка'])
print()


# Печать коллекций

u_1 = User('Спенглер')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]
print(f'{ghostbusters}')
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]
print(repr(ghostbusters))
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]
print(f'{ghostbusters = }')
# ghostbusters = [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]
print(*ghostbusters, sep='\n')
"""
Перед нами Спенглер с пустыми руками. Количество жизней - 3
Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество жизней - 3
Перед нами Стэнц с оборудованием: ловушка, прибор ночного видения. Количество жизней - 3"""
print()


# Задание (что неправильно)

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b
    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'
    def __repr__(self):
        return str(self.a) + str(self.b) + str(self.c)


a = MyClass(1, 2)
print(a) # MyClass(a=1, b=2, c=3)
print(repr(a)) # 123


# Математика и логика в классах

# Сложение через __add__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

a = Vector(2, 4)
b = Vector(3, 7)
c = a + b
print(f'{a = }\t{b = }\t{c = }') #a = Vector(2, 4)        b = Vector(3, 7)        c = Vector(5, 11)


# Сдвиг вправо, __rshift__

from random import choices

class Closet:
    CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')

    def __init__(self, count: int, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'Осталось вещей в шкафу {self.count}:\n{names}'

    def __rshift__(self, other):
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))

storeroom = Closet(10)
print(storeroom)
for _ in range(4):
    storeroom = storeroom >> 3
    print(storeroom)
"""
Осталось вещей в шкафу 10:
брюки, носки, футболка, футболка, туфли, брюки, рубашка, брюки, рубашка, брюки
Осталось вещей в шкафу 7:
носки, футболка, футболка, рубашка, брюки, брюки, носки
Осталось вещей в шкафу 4:
футболка, рубашка, брюки, рубашка
Осталось вещей в шкафу 1:
рубашка
Осталось вещей в шкафу 0:"""


# Умножение текста на “продвинутый текст” методом __rmul__

class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance
    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words)
        return StrPro(result)

text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
# print(s * text) # TypeError: 'str' object cannot be interpreted as an integer


# Вычисление процентов вместо нахождения остатка от деления, __imod__

from decimal import Decimal

class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)
    def __repr__(self):
        return f'Money({self.value:.2f})'
    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self

m = Money(100)
print(m) # Money(100.00)
m %= 50
print(m) # Money(150.00)
m %= 100
print(m) # Money(300.00)


# Задание

class MyClass:
    def __init__(self, data):
        self.data = data
    def __and__(self, other):
        return MyClass(self.data + other.data)
    def __str__(self):
        return str(self.data)

a = MyClass((1, 2, 3, 4, 5))
b = MyClass((2, 4, 6, 8, 10))
print(a & b) # (1, 2, 3, 4, 5, 2, 4, 6, 8, 10)


# Сравнение на идентичность, __eq__

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
print(one == two) # True
print(one == three) # False


# Допустим возможность переворачивания треугольника перед сравнением

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
four = Triangle(4, 3, 5)
print(f'{one == two = }') # one == two = Tru
print(f'{one == three = }') # one == three = True
print(f'{one == four = }') # one == four = True
print(f'{one != one = }') # one != one = False


# Сравнение на больше и меньше,  __lt__

from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'
    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second
    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area
    def __lt__(self, other):
        return self.area() < other.area()

one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²')
print(f'{two} имеет площадь {two.area():.3f} у.е.²')
print(f'{one > two = }\n{one < two = }')
data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
result = sorted(data)
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))
"""
Треугольник со сторонами: 3, 4, 5 имеет площадь 6.000 у.е.²
Треугольник со сторонами: 5, 5, 5 имеет площадь 10.825 у.е.²
one > two = False
one < two = True
[Triangle(3, 5, 3), Triangle(6, 2, 5), Triangle(3, 4, 5), Triangle(4, 4, 4)]
4.146, 4.684, 6.000, 6.928"""


# Неизменяемые экземпляры, хеширование дандер __hash__

# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4,4, 4), Triangle(3, 5, 3)}
# print(triangle_set) #TypeError: unhashable type: 'Triangle'


# Простейшая реализация хэша

from math import sqrt

class Triangle2:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'
    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second
    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area
    def __lt__(self, other):
        return self.area() < other.area()
    def __hash__(self):
        return hash((self._a, self._b, self._c))

triangle_set2 = {Triangle2(3, 4, 5), Triangle2(6, 2, 5), Triangle2(4, 4, 4), Triangle2(3, 5, 3)}
print(triangle_set2) #{Triangle(4, 4, 4), Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(3, 5, 3)}
print(', '.join(f'{hash(item)}' for item in triangle_set2))
# 5958266269407395088, 4003026094496801395, 7248620568795758028, -7050955881463073020


# Задание

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b
    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'
    def __eq__(self, other):
        return (sum((self.a, self.b)) - self.c) == (sum((other.a, other.b)) - other.c)
        # 0 == 0

x = MyClass(42, 2)
y = MyClass(73, 3)
print(x == y) # True


# Обработка атрибутов

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

a = Vector(2, 4)


# Получение значения атрибута, __getattribute__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

a = Vector(2, 4)
# print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')


# Присвоение атрибуту значения, __setattr__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

a = Vector(2, 4)
# print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')
# a.z = 73 # AttributeError: У нас вектор на плоскости, а не в пространстве
a.x = 3
print(f'{a = }')


# Обращение к несуществующему атрибуту, __getattr__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return None

a = Vector(2, 4)
print(a.z) # None
print(f'{a = }')


# Удаление атрибута, __delattr__

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        return None
    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)

a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(f'{a = }, {a.s = }')
"""
a = Vector(2, 4)
a = Vector(2, 4), a.s = 73
a = Vector(0, 4), a.s = None"""


# Функции setattr(), getattr() и delattr()
"""
В Python есть функции, которые позволяют делать тоже
самое, что и рассмотренные выше дандер методы. Разница лишь в том, что метод
реагирует на событие в коде, а функцию вы вызываете в тот момент, когда вам это
нужно.
● setattr(object, name, value) — аналог object.name = value
● getattr(object, name[, default]) — аналог object.name or default
● delattr(object, name) — аналог del object.name"""